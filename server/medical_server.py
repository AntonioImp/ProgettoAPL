from flask import Blueprint, request
import secrets
import string
import datetime
import Class.medicalcenter as med
import Class.doc as doc
import shelve

medical_server = Blueprint("medical_server", __name__, static_folder = "static")
with shelve.open('archive') as archive:
    if "sessionMedical" in archive:
        session = archive['sessionMedical']
    else:
        session = {}
    archive.close()

""" Generatore di token alfanumerici """
def token_generator(size):
    token = ''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(size))
    return token


""" Parametri da passare al metodo login: medName, password"""
@medical_server.route("/login", methods = ["POST"])
def login():
    medName = request.json["medName"]
    medical = med.Medicalcenter(medName)
    if medical.getMedicalcenter() != False and request.json["pass"] == medical.getPassword():
        try:
            for key, value in session.items():
                medId = medical.getMedicalcenter()["id"]
                if value == medId:
                    raise Exception(key) #->"L'utente è già loggato, torno il token"
            
            while True:
                token = token_generator(10)
                if token not in session:
                    break
            session[token] = medId

            with shelve.open('archive') as archive:
                archive['sessionMedical'] = session
                archive.close()
        except Exception as e:
            token = str(e)
        finally:
            res = {}
            res["token"] = token
            for key, value in medical.getMedicalcenter().items():
                if type(value) == int and type(value) == str:
                    res[key] = value
                else:
                    res[key] = str(value)
            print(res)
            return res
    else:
        return "False"


""" Parametri da passare al metodo signup: dati medical center, password"""
@medical_server.route("/signup", methods = ["POST"])
def signup():
    medicalData = {
        "medName": request.json["medName"],
        "p_IVA": request.json["p_IVA"],
        "phone": request.json["phone"],
        "mail": request.json["mail"],
        "CAP": request.json["CAP"],
        "city": request.json["city"],
        "street": request.json["street"],
        "n_cv": request.json["n_cv"]
    }
    medical = med.Medicalcenter(medicalData, request.json["pass"])
    res = medical.insertMedicalcenter()
    if res[0] and res[1]:
        return str(res[2])
    else:
        return "-1" #->"Errore registrazione"


""" Parametri da passare al metodo logout: token """    
@medical_server.route("/logout", methods = ["GET"])
def logout():
    session.pop(request.args["token"])

    with shelve.open('archive') as archive:
        archive['sessionMedical'] = session
        archive.close()
    
    return "0" #->"Logout effettuato"


""" Parametri da passare al metodo updateMedicalcenter: token, dati medical center """
@medical_server.route("/medicalupdate", methods = ["POST"])
def updateMedicalcenter():
    token = request.json["token"]
    if token in session:
        medId = session[token]
        medicalData = {
            "medName": request.json["medName"],
            "p_IVA": request.json["p_IVA"],
            "phone": request.json["phone"],
            "mail": request.json["mail"],
            "CAP": request.json["CAP"],
            "city": request.json["city"],
            "street": request.json["street"],
            "n_cv": request.json["n_cv"]
        }
        medical = med.Medicalcenter(medId)
        if medical.updateMedicalcenter(medicalData) == True:
            return "0" #->"Aggiornamento completato"
        else:
            return "-1" #->"Aggiornamento fallito"
    else:
        return "-2" #->"Autenticazione fallita"


""" Parametri da passare al metodo passupdate: token, nuova password """
@medical_server.route("/passupdate", methods = ["POST"])
def updatePassword():
    token = request.json["token"]
    if token in session:
        medical = med.Medicalcenter(session[token])
        if medical.updatePassword(request.json["pass"]) == True:
            return "0" #->"Password aggiornata"
        else:
            return "-1" #->"Aggiornamento fallito"
    else:
        return "-2" #->"Autenticazione fallita"


""" Parametri da passare al metodo timeupdate: token, start_time, end_time, default_interval 
    Formato tempo: HH:MM:SS """
@medical_server.route("/timeupdate", methods = ["POST"])
def updateTiming():
    token = request.json["token"]
    if token in session:
        medical = med.Medicalcenter(session[token])
        try:
            time_f = '%H:%M:%S'
            datetime.datetime.strptime(request.json["start_time"], time_f)
            datetime.datetime.strptime(request.json["end_time"], time_f)
            datetime.datetime.strptime(request.json["default_interval"], time_f)
        except:
            return "-3" #->"Formato orario errato"
        if medical.updateTiming(request.json["start_time"], request.json["end_time"], request.json["default_interval"]):
            return "0" #->"Tempistiche aggiornata"
        else:
            return "-1" #->"Aggiornamento fallito"
    else:
        return "-2" #->"Autenticazione fallita"


""" Parametri da passare al metodo resetPassword: CF """
@medical_server.route("/passreset", methods = ["POST"])
def resetPassword():
    import smtplib
    from smtplib import SMTPException

    medical = med.Medicalcenter(int(request.json["id"]))
    medicalData = medical.getMedicalcenter()
    if medicalData != False:
        newPass = token_generator(20)
        oldPass = medical.getPassword()
        if medical.updatePassword(newPass):
            messaggio = "From: From Covid-19 Booking System <from@fromdomain.com>\n"
            messaggio += "To: To " + str(medicalData["id"]) + " <" + medicalData["mail"] + ">\n"
            messaggio += "Subject: Reset password for " + str(medicalData["id"]) + "\n\n"
            messaggio += "Hello " + str(medicalData["id"]) + ",\nyour new password is " + newPass + "."
            messaggio += "\n\nThis is an automatic sending system, do not reply to this email."
            try:
                email = smtplib.SMTP("smtp.gmail.com", 587)
                email.ehlo()
                email.starttls()
                email.login("cvhomeworkfinal@gmail.com", "123qwerty@")
                email.sendmail("cvhomeworkfinal@gmail.com", medicalData["mail"], messaggio)
                email.quit()
            except SMTPException:
                medical.updatePassword(oldPass)
                return "-3" #->"Errore invio mail. Password ripristinata all'originale."

            return "0" #->"Password modificata"
        else:
            return "-1" #->"Errore modifica password"
    else:
        return "-2" #->"Utente non trovato"


""" Parametri da passare al metodo delete: token, password """
@medical_server.route("/delete", methods = ["POST"])
def delete():
    token = request.json["token"]
    if token in session:
        medical = med.Medicalcenter(session[token])
        if medical.getPassword() == request.json["pass"]:
            if medical.deleteMedicalcenter() == True:
                session.pop(token)
                return "0" #->"Account eliminato"
            else:
                return "-1" #->"Errore eliminazione"
        else:
            return "-2" #->"Password errata"
    else:
        return "-3" #->"Autenticazione fallita"
    

""" Parametri da passare al metodo insertDoc: token, dati doc """
@medical_server.route("/insertdoc", methods = ["POST"])
def insertDoc():
    token = request.json["token"]
    if token in session:
        medId = session[token]
        docData = {
            'CF': request.json["CF"],
            'name': request.json["name"],
            'surname': request.json["surname"],
            'phone': request.json["phone"],
            'mail': request.json["mail"]
        }
        Doc = doc.Doc(docData)
        days = request.json["days"]
        res = Doc.insertDoc(medId, days)
        if "err" in res:
            return "-1" #->"Errore nell'inserimento. Giorni già impegnati"
        elif "linkIns" in res and not "docIns" in res:
            ret = "1" #->"Dottore già in DB. Aggiunto solo ai dipendenti del medical center"
        else:
            ret = "0" #->"Dottore inserito e assegnato"
        with shelve.open('archive') as archive:
            manager = archive['manager']
            manager.initCalendarDict()
            archive['manager'] = manager
            archive.close()
        return ret
    else:
        return "-2" #->"Autenticazione fallita"

    
""" Parametri da passare al metodo getDocAssignment: token.
    Ritorno:
        {
            indice: docAssignment,
            ...
        }"""
@medical_server.route("/docassignment", methods = ["POST"])
def getDocAssignment():
    token = request.json["token"]
    if token in session:
        res = doc.Doc.getDocAssignment(session[token])
        copyRes = [r.copy() for r in res]
        for cr in copyRes:
            del cr["day"]
        uniqueCopyRes = []
        for x in copyRes:
            if x not in uniqueCopyRes:
                uniqueCopyRes.append(x)
        del copyRes
        for cr in uniqueCopyRes:
            cr["day"] = []
            for d in res:
                if cr["CF"] == d["CF"]:
                    cr["day"].append(d["day"])
        json = {}
        for i, r in enumerate(uniqueCopyRes):
            json[i] = r
        return json
    else:
        return "-2" #->"Autenticazione fallita"


""" Parametri da passare al metodo updateDoc: token, dati doc """
@medical_server.route("/updatedoc", methods = ["POST"])
def updateDoc():
    token = request.json["token"]
    if token in session:
        res = doc.Doc.getDocAssignment(session[token])
        for r in res:
            CF = request.json["CF"]
            if r["CF"] == CF:
                docData = {
                    'CF': CF,
                    'name': request.json["name"],
                    'surname': request.json["surname"],
                    'phone': request.json["phone"],
                    'mail': request.json["mail"]
                }
                Doc = doc.Doc(CF)
                if Doc.updateDoc(docData):
                    return "0" #->"Dottore aggiornato"
        return "-1" #->"Errore aggiornamento"
    else:
        return "-2" #->"Autenticazione fallita"


""" Parametri da passare al metodo dismissDoc: token, CF """
@medical_server.route("/dismissdoc", methods = ["POST"])
def dismissDoc():
    token = request.json["token"]
    if token in session:
        res = doc.Doc.getDocAssignment(session[token])
        CF = request.json["CF"]
        for r in res:
            if r["CF"] == CF:
                Doc = doc.Doc(CF)
                with shelve.open('archive') as archive:
                    manager = archive['manager']
                    archive.close()
                dismiss = Doc.dismissDoc(session[token], manager.getDate())
                if dismiss == True:
                    return "0" #->"Dottore rimosso dai dipendenti"
                elif dismiss == "-1":
                    with shelve.open('archive') as archive:
                        if 'flag' not in archive:
                            archive['flag'] = [(CF, session[token])]
                        else:
                            archive['flag'] += [(CF, session[token])]
                        archive.close()
                    return "-3" #->"Dottore impegnato in prenotazioni"
        return "-1" #->"Errore eliminazione"
    else:
        return "-2" #->"Autenticazione fallita"


"""  --- Gestione prenotazioni ---  """
""" Parametri da passare al metodo getbooked: token """
@medical_server.route("/getbooked", methods = ["POST"])
def getBooked():
    token = request.json["token"]
    if token in session:
        medical = med.Medicalcenter(session[token])
        res = medical.getBooked()
        json = {}
        complete = []
        if res["complete"]:
            for r in res["complete"]:
                r["date"] = str(r["date"])
                r["time"] = str(r["time"])
                r["time_taken"] = str(r["time_taken"])
                complete += [r]
        json["complete"] = complete
        incomplete = []
        if res["incomplete"]:
            for r in res["incomplete"]:
                r["date"] = str(r["date"])
                r["time"] = str(r["time"])
                incomplete += [r]
        json["incomplete"] = incomplete
        return json
    else:
        return "-2" #->"Autenticazione fallita"


""" Parametri da passare al metodo getbooked: token, id prenotazione(id), tempo impiegato(time), risultato(result) """
@medical_server.route("/insertexec", methods=["POST"])
def insertExecution():
    token = request.json["token"]
    if token in session:
        try:
            time_f = '%H:%M:%S'
            datetime.datetime.strptime(request.json["time"], time_f)
        except:
            return "-3" #->"Formato orario errato"
        if request.json["result"] != 'positivo' and request.json["result"] != 'negativo':
            return "-4" #->"Risultato non valido"
        if med.Medicalcenter.insertExecution(request.json["id"], request.json["time"], request.json["result"]):
            return "0" #->"Esecuzione inserita"
        else:
            return "-1" #->"Errore inserimento"
    else:
        return "-2" #->"Autenticazione fallita"


if __name__ == "__main__":
    print(doc.Doc.getDocAssignment(12))
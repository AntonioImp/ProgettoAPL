from flask import Blueprint, request
import secrets
import string
import datetime
import Class.user as u
import Class.medicalcenter as m
import shelve

user_server = Blueprint("user_server", __name__, static_folder = "static")
with shelve.open('archive') as archive:
    if "sessionUser" in archive:
        session = archive['sessionUser']
    else:
        session = {}
    archive.close()

""" Generatore di token alfanumerici """
def token_generator(size):
    token = ''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(size))
    return token

        
""" Parametri da passare al metodo login: CF, password """    
@user_server.route("/login", methods = ["POST"])
def login():
    CF = request.json["CF"]
    user = u.User(CF)
    if user.getUser() != False and user.getPassword() == request.json["pass"]:
        try:
            for key, value in session.items():
                if value == CF:
                    raise Exception(key) #return key #->"L'utente è già loggato, torno il token"
            
            while True:
                token = token_generator(10)
                if token not in session:
                    break
            session[token] = CF

            with shelve.open('archive') as archive:
                archive['sessionUser'] = session
                archive.close()
        except Exception as e:
            token = str(e)
        finally:
            res = {}
            res["token"] = token
            for key, value in user.getUser().items():
                res[key] = value
            return res
    else:
        return "False"


""" Parametri da passare al metodo getuser: token """
@user_server.route("/getuser", methods = ["POST"])
def getUser():
    token = request.json["token"]
    if token in session:
        user = u.User(session[token])
        res = user.getUser()
        if type(res) != bool:
            return res
        else:
            return "-1" #->"Errore identificazione utente"
    else:
        return "-2" #->""Autenticazione fallita""


""" Parametri da passare al metodo signup: dati utente, password """
@user_server.route("/signup", methods = ["POST"])
def signup():
    userData = {'CF': request.json["CF"],
              'name': request.json["name"],
              'surname': request.json["surname"],
              'phone': request.json["phone"],
              'mail': request.json["mail"],
              'age': request.json["age"],
              'CAP': request.json["CAP"],
              'city': request.json["city"],
              'street': request.json["street"],
              'n_cv': request.json["n_cv"]}
    user = u.User(userData, request.json["pass"])
    if user.insertUser() == (True, True):
        return "0" #->"Registrazione effettuata"
    else:
        return "-1" #->"Errore registrazione"


""" Parametri da passare al metodo logout: token """    
@user_server.route("/logout", methods = ["GET"])
def logout():
    session.pop(request.args["token"])

    with shelve.open('archive') as archive:
        archive['sessionUser'] = session
        archive.close()

    return "0" #->"Logout effettuato"


""" Parametri da passare al metodo userupdate: token, dati utente aggiornati """    
@user_server.route("/userupdate", methods = ["POST"])
def updateUser():
    token = request.json["token"]
    if token in session:
        userData = {'CF': session[token],
                    'name': request.json["name"],
                    'surname': request.json["surname"],
                    'phone': request.json["phone"],
                    'mail': request.json["mail"],
                    'age': request.json["age"],
                    'CAP': request.json["CAP"],
                    'city': request.json["city"],
                    'street': request.json["street"],
                    'n_cv': request.json["n_cv"]}
        user = u.User(session[token])
        if user.updateUser(userData) == True:
            return "0" #->"Aggiornamento completato"
        else:
            return "-1" #->"Aggiornamento fallito"
    else:
        return "-2" #->"Autenticazione fallita"
    
    
""" Parametri da passare al metodo passupdate: token, nuova password """
@user_server.route("/passupdate", methods = ["POST"])
def updatePassword():
    token = request.json["token"]
    if token in session:
        user = u.User(session[token])
        if user.updatePassword(request.json["pass"]):
            return "0" #->"Password aggiornata"
        else:
            return "-1" #->"Aggiornamento fallito"
    else:
        return "-2" #->"Autenticazione fallita"
    

""" Parametri da passare al metodo resetPassword: CF """
@user_server.route("/passreset", methods = ["POST"])
def resetPassword():
    import smtplib
    from smtplib import SMTPException

    user = u.User(request.json["CF"])
    userData = user.getUser()
    if userData != False:
        newPass = token_generator(20)
        oldPass = user.getPassword()
        if user.updatePassword(newPass):
            messaggio = "From: From Covid-19 Booking System <from@fromdomain.com>\n"
            messaggio += "To: To " + userData["CF"] + " <" + userData["mail"] + ">\n"
            messaggio += "Subject: Reset password for " + userData["CF"] + "\n\n"
            messaggio += "Hello " + userData["CF"] + ",\nyour new password is " + newPass + "."
            messaggio += "\n\nThis is an automatic sending system, do not reply to this email."
            try:
                email = smtplib.SMTP("smtp.gmail.com", 587)
                email.ehlo()
                email.starttls()
                email.login("cvhomeworkfinal@gmail.com", "123qwerty@")
                email.sendmail("cvhomeworkfinal@gmail.com", userData["mail"], messaggio)
                email.quit()
            except SMTPException:
                user.updatePassword(oldPass)
                return "-3" #->"Errore invio mail. Password ripristinata all'originale."

            return "0" #->"Password modificata"
        else:
            return "-1" #->"Errore modifica password"
    else:
        return "-2" #->"Utente non trovato"


""" Parametri da passare al metodo delete: token, password """
@user_server.route("/delete", methods = ["POST"])
def delete():
    token = request.json["token"]
    if token in session:
        user = u.User(session[token])
        if user.getPassword() == request.json["pass"]:
            if user.deleteUser() == True:
                session.pop(token)
                return "0" #->"Account eliminato"
            else:
                return "-1" #->"Errore eliminazione"
        else:
            return "-3" #->"Password errata"
    else:
        return "-2" #->"Autenticazione fallita"


"""  --- GESTIONE PRENOTAZIONI ---  """
""" Parametri da passare al metodo bookingMedicalcenter: token.
    Ritorno:
        {
            indice: medicalcenter,
            ...
        }"""
@user_server.route("/getmedical", methods = ["POST"])
def bookingMedicalcenter():
    token = request.json["token"]
    if token in session:
        res = m.Medicalcenter.getMedicalcenters()
        json = {}
        for i, medical in enumerate(res):
            json[i] = medical
        return json
    else:
        return "-2" #->"Autenticazione fallita"


""" Parametri da passare al metodo getcalendar: token, id medical center(id)
    Ritorna un dict:
    {
        CF medico: lista orari,
        ...
    } """
@user_server.route("/getcalendar", methods = ["POST"])
def getCalendar():
    token = request.json["token"]
    if token in session:
        with shelve.open('archive') as archive:
            manager = archive['manager']
            archive.close()
        calendarDict = manager.getCalendarDict()
        if not calendarDict:
            return "-1" #->"Non si effettuano tamponi la domenica o non è presente alcun medical center"
        res = calendarDict[int(request.json["id"])].getCalendar()
        if res != False:
            json = {}
            for doc, turn  in res.items():
                json[doc] = [str(t) for t in turn]
            return json
        else:
            return "-3" #->"Nessun dottore disponibile"
    else:
        return "-2" #->"Autenticazione fallita"


""" Parametri da passare al metodo setBooking: token, id medical center(id), ora prenotazione(time), CF dottore(CF_M)
    Formato data tempo: YYYY-MM-DD HH:MM:SS """
@user_server.route("/setbooking", methods = ["POST"])
def setBooking():
    token = request.json["token"]
    if token in session:
        with shelve.open('archive') as archive:
            manager = archive['manager']
            archive.close()
        calendarDict = manager.getCalendarDict()
        
        if not calendarDict:
            return "-5" #->"Non si effettuano tamponi la domenica"
        
        try:
            date_f = '%H:%M:%S'
            dt = datetime.datetime.strptime(str(request.json["time"]), date_f)
            dt.time().replace(second=0)
        except:
            return "-1" #->"Datetime format error"
        
        user = u.User(session[token])
        booked = user.getBooked()
        for b in booked:
            if b["date"] == manager.getDate():
                return "-6" #->"L'utente ha già una prenotazione per questo giorno"
        del booked

        booking = {
            "CF": session[token],
            "id": int(request.json["id"]),
            "CF_M": request.json["CF_M"],
            "date": manager.getDate(),
            "time": dt.time()
        }
        if not manager.removeBooked(int(request.json["id"]), dt, request.json["CF_M"]):
            return "-3" #->"Errore aggiornamento calendario"
        res = user.insertBooking(booking)
        if res["ins"]:
            with shelve.open('archive') as archive:
                archive['manager'] = manager
                archive.close()
            return str(res["lastId"]) #->"Prenotazione inserita, torna l'id"
        else:
            return "-4" #->"Errore inserimento prenotazione"
    else:
        return "-2" #->"Autenticazione fallita"


""" Parametri da passare al metodo getbooked: token """
@user_server.route("/getbooked", methods = ["POST"])
def getBooked():
    token = request.json["token"]
    if token in session:
        user = u.User(session[token])
        res = user.getBookedComplete()
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


""" Parametri da passare al metodo deleteBooked: token, id prenotazione (id) """
@user_server.route("/deletebooked", methods = ["POST"])
def deleteBooked():
    token = request.json["token"]
    if token in session:
        user = u.User(session[token])
        res = user.getBooked()
        res2 = None
        for r in res:
            if r["practical_num"] == int(request.json["id"]):
                res2 = user.deleteBooked(int(request.json["id"]))
        if res2 == None:
            return "-1" #->"Prenotazione non trovata"
        elif res2:
            return "0" #->"Prenotazione eliminata"
        else:
            return "-3" #->"Errore nell'eliminazione, il tampone potrebbe già essere stato eseguito"
    else:
        return "-2" #->"Autenticazione fallita"


if __name__ == "__main__":
    user_server.run()
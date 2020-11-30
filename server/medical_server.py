from flask import Blueprint, request
import secrets
import string
import Class.medicalcenter as med
import Class.doc as doc
import smtplib
from smtplib import SMTPException

medical_server = Blueprint("medical_server", __name__, static_folder = "static")
session = {}

""" Generatore di token alfanumerici """
def token_generator(size):
    token = ''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(size))
    return token


""" Parametri da passare al metodo login: id, password"""
@medical_server.route("/login", methods = ["POST"])
def login():
    medId = request.json["id"]
    medical = med.Medicalcenter(medId)
    if medical.getMedicalcenter() != False and request.json["pass"] == medical.getPassword():
        token = token_generator(10)
        session[token] = medId
        return token
    else:
        return "False"


""" Parametri da passare al metodo signup: dati medical center, password"""
@medical_server.route("/signup", methods = ["POST"])
def signup():
    medicalData = {
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
        return "False"


""" Parametri da passare al metodo logout: token """    
@medical_server.route("/logout", methods = ["GET"])
def logout():
    session.pop(request.args["token"])
    return "0" #->"Logout effettuato"


""" Parametri da passare al metodo updateMedicalcenter: token, dati medical center """
@medical_server.route("/medicalupdate", methods = ["POST"])
def updateMedicalcenter():
    token = request.json["token"]
    if token in session:
        medId = session[token]
        medicalData = {
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
        return "-3" #->"Autenticazione fallita"


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


""" Parametri da passare al metodo resetPassword: CF """
@medical_server.route("/passreset", methods = ["POST"])
def resetPassword():
    medical = med.Medicalcenter(request.json["id"])
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
        res = Doc.insertDoc(medId)
        if len(res) == 1 and res[0] == True:
            return "1" #->"Dottore già in DB. Aggiunto solo ai dipendenti del medical center"
        elif len(res) == 2 and res[0] == True and res[1] == True:
            return "0" #->"Dottore inserito"
        else:
            return "-1" #->"Errore nell'inserimento"
    else:
        return "-2" #->"Autenticazione fallita"

    
""" Parametri da passare al metodo getDocAssignment: token"""
@medical_server.route("/docassignment", methods = ["POST"])
def getDocAssignment():
    token = request.json["token"]
    if token in session:
        res = doc.Doc.getDocAssignment(session[token])
        json = "{"
        for r in res:
            json += str(r)
        json += "}"
        return json
    else:
        return "-1" #->"Autenticazione fallita"


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
                    return "True"
        return "False"
    else:
        return "Autenticazione fallita"


""" Parametri da passare al metodo dismissDoc: token, CF """
@medical_server.route("/dismissdoc", methods = ["POST"])
def dismissDoc():
    token = request.json["token"]
    if token in session:
        res = doc.Doc.getDocAssignment(session[token])
        for r in res:
            CF = request.json["CF"]
            if r["CF"] == CF:
                Doc = doc.Doc(CF)
                if Doc.dismissDoc(session[token]):
                    return "Dottore rimosso dai dipendenti"
        return "False"
    else:
        return "Autenticazione fallita"


if __name__ == "__main__":
    print(doc.Doc.getDocAssignment(12))
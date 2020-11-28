from flask import Blueprint, request
import secrets
import string
import Class.user as u

user_server = Blueprint("user_server", __name__, static_folder = "static")
session = {}

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
        token = token_generator(10)
        session[token] = CF
        return token
    else:
        return "False"


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
        return "True"
    else:
        return "False"

    
""" Parametri da passare al metodo logout: token """    
@user_server.route("/logout", methods = ["GET"])
def logout():
    session.pop(request.args["token"])
    return "True"


""" Parametri da passare al metodo userupdate: token, dati utente aggiornati """    
@user_server.route("/userupdate", methods = ["POST"])
def updateUser():
    token = request.json["token"]
    if token in session:
        if session[token] == request.json["CF"]:
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
            user = u.User(session[token])
            if user.updateUser(userData) == True:
                return "0" #->"Aggiornamento completato"
            else:
                return "-1" #->"Aggiornamento fallito"
        else:
            return "-2" #->"Codice Fiscale non modificabile"
    else:
        return "-3" #->"Autenticazione fallita"
    
    
""" Parametri da passare al metodo passupdate: token, nuova password """
@user_server.route("/passupdate", methods = ["POST"])
def updatePassword():
    token = request.json["token"]
    if token in session:
        user = u.User(session[token])
        if user.updatePassword(request.json["pass"]) == True:
            return "0" #->"Password aggiornata"
        else:
            return "-1" #->"Aggiornamento fallito"
    else:
        return "-3" #->"Autenticazione fallita"
    

""" Parametri da passare al metodo delete: token, password """
@user_server.route("/delete", methods = ["POST"])
def delete():
    token = request.json["token"]
    if token in session:
        user = u.User(session[token])
        if user.getPassword() == request.json["pass"]:
            if user.deleteUser() == True:
                return "0" #->"Account eliminato"
            else:
                return "-1" #->"Errore eliminazione"
        else:
            return "-2" #->"Password errata"
    else:
        return "-3" #->"Autenticazione fallita"
    

if __name__ == "__main__":
    user_server.run()
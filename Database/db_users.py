import sys

sys.path.append('../')
import Database.db_access as db_access

db = db_access.DBHelper()

def getUsers():
    return db.fetch("select * from users")

def getUser(CF):
    query = "select * from users where CF = '" + CF + "'"
    return db.fetch(query)

def getPassword(CF):
    query = "select password from credentials where username = '" + CF + "'"
    return db.fetch(query)

def insertUser(user, password):
    query = "INSERT INTO users(CF, name, surname, phone, mail, age, CAP, city, street, n_cv)"
    query += " VALUES ('" + user["CF"] + "','" + user["name"] + "','" + user["surname"] + "','" + user["phone"]
    query += "','" + user["mail"] + "'," + str(user["age"]) + ",'" + user["CAP"] + "','" + user["city"] + "','"
    query += user["street"] + "'," + str(user["n_cv"]) + ")"
    query2 = "INSERT INTO credentials(username, password) VALUES ('" + user["CF"] + "', '" + password + "')"
    return db.execute(query), db.execute(query2)

def updateUser(CF, user):
    query = "UPDATE users SET CF = '" + user["CF"] + "', name = '" + user["name"] + "', surname = '" + user["surname"]
    query += "', phone = '" + user["phone"] + "', mail = '" + user["mail"] + "', age = '" + str(user["age"]) + "', CAP = '"
    query += user["CAP"] + "', city = '" + user["city"] + "', street = '" + user["street"]
    query += "', n_cv = '" + str(user["n_cv"]) + "' WHERE CF = '" + CF + "'"
    return db.execute(query)

def updatePassword(CF, password):
    query = "UPDATE credentials SET password='" + password + "' WHERE username = '" + CF + "'"
    return db.execute(query)

def deleteUser(CF):
    query = "DELETE FROM users WHERE CF = '" + CF + "'"
    return db.execute(query)

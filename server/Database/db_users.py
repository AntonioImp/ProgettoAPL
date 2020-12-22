import sys

sys.path.append('../')
import Database.db_access as db_access

db = db_access.DBHelper()


"""  --- CRUD OP ---  """
def getUsers():
    func = db.select([], "users", [], [""])
    return func()

def getUser(CF):
    func = db.select([], "users", [("CF", "=", CF)], [""])
    return func()

def getPassword(CF):
    func = db.select(["password"], "credentials", [("username", "=", CF)], [""])
    return func()

def insertUser(user, password):
    func = db.insert(user, "users", False)
    res1 = func()
    credential = {"username": user["CF"], "password": password}
    func = db.insert(credential, "credentials", False)
    res2 = func()
    return res1, res2

def updateUser(CF, user):
    func = db.update(user,"users", [("CF", "=", CF)], [""], False)
    return func()

def updatePassword(CF, password):
    func = db.update({"password": password}, "credentials", [("username", "=", CF)], [""], False)
    return func()

def deleteUser(CF):
    func = db.delete("users", [("CF", "=", CF)], [""], False)
    return func()

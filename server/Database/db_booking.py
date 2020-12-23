import sys

sys.path.append("../")
import Database.db_access as db_access

db = db_access.DBHelper()

def getAllBooked():
    # query = "SELECT * FROM booking"
    func = db.select([], "booking", [], [""])
    return func()

def getBooked(entity, name):
    if entity == "user":
        # query = "SELECT * FROM booking WHERE CF_U = '" + name + "'"
        func = db.select([], "booking", [("CF_U", "=", name)], [""])
    elif entity == "medical":
        # query = "SELECT * FROM booking WHERE ID_M = " + str(name)
        func = db.select([], "booking", [("ID_M", "=", name)], [""])
    return func()

def insertBooking(booking):
    # query = "INSERT INTO booking(CF_U, ID_M, CF_M, date, time) VALUES ('" + booking["CF"]
    # query += "', " + str(booking["id"]) + ", '" + booking["CF_M"] + "', '" + str(booking["date"]) + "', '" + str(booking["time"]) + "')"
    func = db.insert(booking, "booking", False)
    res = {}
    res["ins"] = func()
    res["lastId"] = db.lastInsertId()
    return res

def insertExecutions(id, time_taken, result):
    # query = "UPDATE booking SET time_taken = '" + time_taken + "', result = '" + result + "' WHERE practical_num = " + str(id)
    func = db.update({"time_taken": time_taken, "result": result}, "booking", [("practical_num", "=", id)], [""], False)
    if func():
        # query = "SELECT * FROM booking"
        func = db.select([], "booking", [("practical_num", "=", id)], [""])
        return func()
    else:
        return False

def deleteBooked(practical_num):
    # query = "DELETE FROM booking WHERE practical_num = " + str(practical_num)
    func = db.delete("booking", [("practical_num", "=", practical_num)], [""], False)
    return func()
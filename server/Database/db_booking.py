import sys

sys.path.append("../")
import Database.db_access as db_access

db = db_access.DBHelper()

def getAllBooked():
    func = db.select([], "booking", [], [""])
    return func()

def getBooked(entity, name):
    if entity == "user":
        func = db.select([], "booking", [("CF_U", "=", name)], [""])
    elif entity == "medical":
        func = db.select([], "booking", [("ID_M", "=", name)], [""])
    return func()

def insertBooking(booking):
    func = db.insert(booking, "booking", False)
    res = {}
    res["ins"] = func()
    res["lastId"] = db.lastInsertId()
    return res

def insertExecutions(id, time_taken, result):
    func = db.update({"time_taken": time_taken, "result": result}, "booking", [("practical_num", "=", id)], [""], False)
    if func():
        func = db.select([], "booking", [("practical_num", "=", id)], [""])
        return func()
    else:
        return False

def deleteBooked(practical_num):
    func = db.delete("booking", [("practical_num", "=", practical_num)], [""], False)
    return func()
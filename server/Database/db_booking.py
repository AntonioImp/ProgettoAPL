import sys

sys.path.append("../")
import Database.db_access as db_access

db = db_access.DBHelper()

def getAllBooked():
    query = "SELECT * FROM booking"
    return db.fetch(query)

def getBooked(entity, name):
    if entity == "user":
        query = "SELECT * FROM booking WHERE CF_U = '" + name + "'"
    elif entity == "medical":
        query = "SELECT * FROM booking WHERE ID_M = " + name
    return db.fetch(query)

def insertBooking(booking):
    query = "INSERT INTO booking(CF_U, ID_M, CF_M, date, time) VALUES ('" + booking["CF"]
    query += "', " + str(booking["id"]) + ", '" + booking["CF_M"] + "', '" + str(booking["date"]) + "', '" + str(booking["time"]) + "')"
    res = {}
    res["ins"] = db.execute(query)
    res["lastId"] = db.lastInsertId()
    return res

def insertExecutions(id, time_taken, result):
    query = "UPDATE booking SET time_taken = '" + time_taken + "', result = '" + result + "' WHERE practical_num = " + str(id)
    if db.execute(query):
        query = "SELECT * FROM booking"
        return db.fetch(query)
    else:
        return False

def deleteBooked(practical_num):
    query = "DELETE FROM booking WHERE practical_num = " + str(practical_num)
    return db.execute(query)
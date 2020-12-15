import sys

sys.path.append('../')
import Database.db_access as db_access

db = db_access.DBHelper()

def getMedicalcenters():
    return db.fetch("SELECT id, phone, mail, CAP, city, street, n_cv FROM medical_centers")

def getMedicalcenter(medId):
    query = "SELECT * FROM medical_centers WHERE id = " + str(medId)
    return db.fetch(query)

def getPassword(medId):
    query = "SELECT password FROM medical_center_credentials WHERE id = " + str(medId)
    return db.fetch(query)

def getBooked(medId):
    res = {}
    query = "SELECT * FROM booking WHERE ID_M = " + str(medId)
    res["booked"] = db.fetch(query)
    query = "SELECT * FROM executions"
    res["execution"] = db.fetch(query)
    return res

def insertMedicalcenter(mc, password):
    query = "INSERT INTO medical_centers(p_IVA, phone, mail, CAP, city, street, n_cv)"
    query += " VALUES ( '" + mc["p_IVA"] + "', '" + mc["phone"] + "', '" + mc["mail"]
    query += "', '" + mc["CAP"] + "', '" + mc["city"] + "', '" + mc["street"] + "', " + str(mc["n_cv"]) + ")"
    res = (db.execute(query),)
    lastId = db.lastInsertId()
    query2 = "INSERT INTO medical_center_credentials(id, password) VALUES ( " + str(lastId) + ", '" + password + "' )"
    res += (db.execute(query2), lastId)
    return res

def updateMedicalcenter(medId, mc):
    query = "UPDATE medical_centers SET p_IVA='" + mc["p_IVA"] + "',phone='" + mc["phone"] + "',mail='" + mc["mail"]
    query += "',CAP='" + mc["CAP"] + "',city='" + mc["city"] + "',street='" + mc["street"] + "',n_cv='" + str(mc["n_cv"]) 
    query += "' WHERE id = " + str(medId)
    return db.execute(query)

def updatePassword(medId, password):
    query = "UPDATE medical_center_credentials SET password='" + password + "' WHERE id=" + str(medId)
    return db.execute(query)

def updateTiming(medId, start_time, end_time, default_interval):
    query = "UPDATE medical_centers SET start_time='" + str(start_time) + "', end_time='" + str(end_time) + "', default_interval='" 
    query += str(default_interval) + "' WHERE id=" + str(medId)
    return db.execute(query)

def deleteMedicalcenter(medId):
    query = "DELETE FROM medical_centers WHERE id = " + str(medId)
    return db.execute(query)

def insertExecutions(id, time_taken, result):
    query = "INSERT INTO executions(id, time_taken, result) VALUES (" + str(id) + ",'" + time_taken + "','" + result + "')"
    return db.execute(query)

if __name__ == "__main__":
    #print(getMedicalcenters())
    #print(getMedicalcenter(17))
    #print(getPassword(1))
    """print(insertMedicalcenter({
        "p_IVA": "A",
        "phone": "A",
        "mail": "A",
        "CAP": "A",
        "city": "A",
        "street": "A",
        "n_cv": 24
    }, "C"))
    print(updateMedicalcenter(17, {
        "p_IVA": "F",
        "phone": "F",
        "mail": "F",
        "CAP": "F",
        "city": "F",
        "street": "F",
        "n_cv": 24
    }))
    print(updatePassword(7, "C"))
    print(deleteMedicalcenter(7))
    print(updateTiming(17, '09:00:00', '11:00:00', '00:15:00'))
    tup = getMedicalcenter(17)
    for t in tup:
        print(t["default_interval"])"""
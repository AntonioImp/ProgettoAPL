import sys

sys.path.append('../')
import Database.db_access as db_access

db = db_access.DBHelper()

# #select(["name", "ID_M"], "booking", [("CF", "==", CF), ("name", "!=", name)], ["AND", ""])
# #insert({"name": "CF", "ID_M": "name"}, "booking", False)
# #update({"name": "CF", "ID_M": "name"}, "booking", [("id", "=", "A")], [""], False)
# #delete("medical_centers", [("id", "=", medId)], [""], False)

def getMedicalcenters():
    func = db.select(["id", "medical_name", "phone", "mail", "CAP", "city", "street", "n_cv"], "medical_centers", [], [""])
    return func()

def getMedicalcenter(med):
    if type(med) == str:
        func = db.select([], "medical_centers", [("medical_name", "=", str(med))], [""])
    else:
        func = db.select([], "medical_centers", [("id", "=", str(med))], [""])
    return func()

def getPassword(medId):
    func = db.select(["password"], "medical_center_credentials", [("id", "=", str(medId))], [""])
    return func()

def insertMedicalcenter(mc, password):
    func = db.insert(mc, "medical_centers", False)
    res = (func(),)
    lastId = db.lastInsertId()
    credential = {"id": lastId, "password": password}
    func = db.insert(credential, "medical_center_credentials", False)
    res += (func(), lastId)
    return res

def updateMedicalcenter(medId, mc):
    func = db.update(mc, "medical_centers", [("id", "=", medId)], [""], False)
    return func()

def updatePassword(medId, password):
    func = db.update({"password": password}, "medical_center_credentials", [("id", "=", medId)], [""], False)
    return func()

def updateTiming(medId, start_time, end_time, default_interval):
    data = {
        "start_time": start_time,
        "end_time": end_time,
        "default_interval": default_interval
    }
    func = db.update(data, "medical_centers", [("id", "=", medId)], [""], False)
    return func()

def deleteMedicalcenter(medId):
    func = db.delete("medical_centers", [("id", "=", medId)], [""], False)
    return func()

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
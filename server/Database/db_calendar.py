import sys

sys.path.append("../")
import Database.db_access as db_access

db = db_access.DBHelper()

def startCalendar(medId):
    query = "SELECT CF FROM docs_list WHERE id = " + str(medId)
    docs = set([doc["CF"] for doc in db.fetch(query)])
    res = []
    for doc in docs:
        query = "SELECT * FROM doc_timing WHERE CF = '" + doc +"'"
        d = db.fetch(query)
        if d != ():
            for tmp in d:
                res += d
    query = "SELECT id, start_time, end_time, default_interval FROM medical_centers WHERE id = " + str(medId)
    med = db.fetch(query)
    return med[0], res, docs

def getBooked(medId):
    query = "SELECT * FROM booking WHERE ID_M = " + str(medId)
    return db.fetch(query)

if __name__ == "__main__":
    print(startCalendar(15))

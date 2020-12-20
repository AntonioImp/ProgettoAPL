import sys

sys.path.append("../")
import Database.db_access as db_access

db = db_access.DBHelper()

def startCalendar(medId, day):
    query = "SELECT CF FROM docs_list WHERE id = " + str(medId) + " AND day = '" + day + "'"
    docs = set([doc["CF"] for doc in db.fetch(query)])
    docs_time = {}
    for doc in docs:
        query = "SELECT avarage_time FROM docs WHERE CF = '" + doc +"'"
        d = db.fetch(query)[0]
        if d['avarage_time'] != None:
            docs_time[doc] = d['avarage_time']
    query = "SELECT id, start_time, end_time, default_interval FROM medical_centers WHERE id = " + str(medId)
    med = db.fetch(query)
    return med[0], docs_time, docs

def getBooked(medId):
    query = "SELECT * FROM booking WHERE ID_M = " + str(medId)
    return db.fetch(query)


if __name__ == "__main__":
    print(startCalendar(15, "lunedì"))

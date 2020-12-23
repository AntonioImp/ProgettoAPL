import sys

sys.path.append("../")
import Database.db_access as db_access

db = db_access.DBHelper()

def startCalendar(medId, day):
    func = db.select(["CF"], "docs_list", [("id", "=", medId), ("day", "=", day)], ["AND", ""])
    docs = set([doc["CF"] for doc in func()])
    docs_time = {}
    for doc in docs:
        func = db.select(["avarage_time"], "docs", [("CF", "=", doc)], [""])
        d = func()[0]
        if d['avarage_time'] != None:
            docs_time[doc] = d['avarage_time']
    func = db.select(["id", "start_time", "end_time", "default_interval"], "medical_centers", [("id", "=", medId)], [""])
    med = func()
    return med[0], docs_time, docs

def getBooked(medId):
    func = db.select([], "booking", [("ID_M", "=", medId)], [""])
    return func()


if __name__ == "__main__":
    print(startCalendar(15, "lunedì"))

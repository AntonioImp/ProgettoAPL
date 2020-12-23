import sys

sys.path.append('../')
import Database.db_access as db_access

db = db_access.DBHelper()

def getDocs():
    func = db.select([], "docs", [], [""])
    return func()

def getDoc(CF):
    func = db.select([], "docs", [("CF", "=", CF)], [""])
    return func()

def getDocAssignment(medId):
    func1 = db.select([], "docs_list", [("id", "=", medId)], [""])
    func2 = db.select([], "docs", [], [""])
    return func1(), func2()

def insertDoc(medId, doc, days):
    res = {}
    if getDoc(doc["CF"]) == ():
        func = db.insert(doc, "docs", False)
        res["docIns"] = func()
    
    if db.startTransaction():
        for day in days:
            func = db.insert({"CF": doc["CF"], "day": day, "id": medId}, "docs_list", True)
            insertLink = func()
            if not insertLink:
                res["err"] = "Doc already assig in " + day
                return res
        if db.stopTransaction():
            res["linkIns"] = "Doc assig"
            
    return res

def updateDoc(CF, doc):
    func = db.update(doc, "docs", [("CF", "=", CF)], [""], False)
    return func()

def deleteDoc(CF):
    func = db.delete("docs", [("CF", "=", CF)], [""], False)
    return func()

def dismissDoc(CF, medId):
    func = db.delete("docs_list", [("CF", "=", CF), ("id", "=", medId)], ["AND", ""], False)
    return func()

def controlDismissDoc(CF):
    func = db.select([], "booking", [("CF_M", "=", CF)], [""])
    return func()

    
if __name__ == "__main__":
    print(getDocs())
    print(getDoc('A'))
    """print(insertDoc(12, {'CF': 'D',
                  'name': 'D',
                  'surname': 'D',
                  'phone': 'D',
                  'mail': 'D'}))
    print(updateDoc('B', {'CF': 'B',
                  'name': 'C',
                  'surname': 'C',
                  'phone': 'C',
                  'mail': 'C'}))
    print(deleteDoc('B'))
    print(getDocAssignment(1))
    print(getDocAssignment('B'))
    print(getDocAssignment(1, 'B'))
    print(getDocAssignment('B', 1))
    print(getDocAssignment())
    print(dismissDoc('B', 10))"""
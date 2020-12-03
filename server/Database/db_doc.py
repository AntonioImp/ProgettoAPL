import sys

sys.path.append('../')
import Database.db_access as db_access

db = db_access.DBHelper()

def getDocs():
    query = "SELECT * FROM docs"
    return db.fetch(query)

def getDoc(CF):
    query = "SELECT * FROM docs WHERE CF = '" + CF + "'"
    return db.fetch(query)

def getDocAssignment(data):
    if len(data) == 0:
        query = "SELECT l.id, l.day, d.CF, d.name, d.surname, d.phone, d.mail FROM docs_list AS l INNER JOIN docs AS d ON l.CF = d.CF"
    elif len(data) == 1:
        if type(data[0]) == str:
            query = "SELECT l.id, l.day, d.CF, d.name, d.surname, d.phone, d.mail FROM docs_list AS l "
            query += "INNER JOIN docs AS d ON l.CF = d.CF WHERE d.CF = '" + data[0] + "'"
        else:
            query = "SELECT l.id, l.day, d.CF, d.name, d.surname, d.phone, d.mail FROM docs_list AS l "
            query += "INNER JOIN docs AS d ON l.CF = d.CF WHERE l.id = " + str(data[0])
    else:
        if type(data[0]) == str:
            query = "SELECT l.id, l.day, d.CF, d.name, d.surname, d.phone, d.mail FROM docs_list AS l "
            query += "INNER JOIN docs AS d ON l.CF = d.CF WHERE d.CF = '" + data[0] + "' AND l.id = " + str(data[1])
        else:
            query = "SELECT l.id, l.day, d.CF, d.name, d.surname, d.phone, d.mail FROM docs_list AS l "
            query +="INNER JOIN docs AS d ON l.CF = d.CF WHERE d.CF = '" + data[1] + "' AND l.id = " + str(data[0])
    return db.fetch(query)

def insertDoc(medId, doc, days):
    res = {}
    if getDoc(doc["CF"]) == ():
        query = "INSERT INTO docs(CF, name, surname, phone, mail)"
        query += " VALUES ('" + doc["CF"] + "','" + doc["name"] + "','" + doc["surname"] + "','" + doc["phone"]
        query += "','" + doc["mail"] + "')"
        res["docIns"] = db.execute(query)
    
    if db.startTransaction():
        for day in days:
            query = "INSERT INTO docs_list(CF, day, id) VALUES ('" + doc["CF"] + "', '" + day + "', " + str(medId) + ")"
            insertLink = db.transactionQuery(query)
            if not insertLink:
                res["err"] = "Doc already assig in " + day
                return res
        if db.stopTransaction():
            res["linkIns"] = "Doc assig"
            
    return res

def updateDoc(CF, doc):
    query = "UPDATE docs SET CF = '" + doc["CF"] + "', name = '" + doc["name"] + "', surname = '" + doc["surname"]
    query += "', phone = '" + doc["phone"] + "', mail = '" + doc["mail"] + "' WHERE CF = '" + CF + "'"
    return db.execute(query)

def deleteDoc(CF):
    query = "DELETE FROM docs WHERE CF = '" + CF + "'"
    return db.execute(query)

def dismissDoc(CF, medId):
    query = "DELETE FROM docs_list WHERE CF = '" + CF + "' AND id = " + str(medId)
    return db.execute(query)
    
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
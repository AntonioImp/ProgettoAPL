from dotenv import load_dotenv
from os import getenv
import pymysql

class DBHelper:

    def __init__(self):
        load_dotenv(dotenv_path='../.env')

    def __connect__(self):
        self.con = pymysql.connect(host=getenv("HOSTNAME"),
                                   user=getenv("DBUSER"),
                                   password=getenv("DBPASS"),
                                   db=getenv("DBNAME"),
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        try:
            self.__connect__()
            self.cur.execute(sql)
            result = self.cur.fetchall()
            self.__disconnect__()
            return result
        except Exception as arg:
            print(arg)
            self.con.rollback()
            return False

    def execute(self, sql):
        try:
            self.__connect__()
            self.cur.execute(sql)
            self.con.commit()
            self.__disconnect__()
            return True
        except Exception as arg:
            print(arg)
            self.con.rollback()
            return False
        
    def lastInsertId(self):
        return self.cur.lastrowid

    def startTransaction(self):
        try:
            self.__connect__()
            return True
        except Exception as arg:
            print(arg)
            return False
    
    def transactionQuery(self, sql):
        try:
            self.cur.execute(sql)
            return True
        except Exception as arg:
            print(arg)
            self.con.rollback()
            return False
    
    def stopTransaction(self):
        try:
            self.con.commit()
            self.__disconnect__()
            return True
        except Exception as arg:
            print(arg)
            self.con.rollback()
            return False

    #func = select(["name", "ID_M"], "booking", [("CF", "==", CF), ("name", "!=", name)], ["AND", ""])
    def select(self, param, table, filt, logic):
        def queryGenerator():
            query = "SELECT "
            if len(param) == 0:
                query += "*"
            else:
                query += str(param.pop(0))
                for p in param:
                    query += ", " + str(p)
            query += " FROM " + table
            if len(filt) != 0:
                query += " WHERE "
                for i, f in enumerate(filt):
                    query += str(f[0]) + " " + str(f[1]) + " '" + str(f[2]) + "'"
                    if logic[i] != "":
                        query += " " + str(logic[i]) + " "
            print(query)
            return self.fetch(query)
        return queryGenerator

    #insert({"name": "CF", "ID_M": "name"}, "booking", False)
    def insert(self, data, table, trans):
        key = list(data.keys())
        val = list(data.values())
        def queryGenerator():
            query = "INSERT INTO " + table + "(" + str(key.pop(0))
            for k in key:
                query += ", " + str(k)
            query += ") VALUES ('" + str(val.pop(0))
            for v in val:
                query += "', '" + str(v)
            query += "')"
            print(query)
            if trans:
                return self.transactionQuery(query)
            else:
                return self.execute(query)
        return queryGenerator
    
    #update({"name": "CF", "ID_M": "name"}, "booking", [("id", "=", "A")], [""], False)
    def update(self, data, table, filt, logic, trans):
        item = list(data.items())
        def queryGenerator():
            query = "UPDATE " + table + " SET " + str(item[0][0]) + "='" + str(item[0][1])
            del item[0]
            for i in item:
                query += "', " + str(i[0]) + "='" + str(i[1])
            query += "' WHERE "
            for i, f in enumerate(filt):
                query += str(f[0]) + " " + str(f[1]) + " " + str(f[2])
                if logic[i] != "":
                    query += " " + str(logic[i]) + " "
            print(query)
            if trans:
                return self.transactionQuery(query)
            else:
                return self.execute(query)
        return queryGenerator
    
    #delete("booking", [("id", "=", "A")], [""], False)
    def delete(self, table, filt, logic, trans):
        def queryGenerator():
            query = "DELETE FROM " + table + " WHERE "
            for i, f in enumerate(filt):
                query += str(f[0]) + " " + str(f[1]) + " " + str(f[2])
                if logic[i] != "":
                    query += " " + str(logic[i]) + " "
            print(query)
            if trans:
                return self.transactionQuery(query)
            else:
                return self.execute(query)
        return queryGenerator
import pymysql

class DBHelper:

    def __init__(self):
        self.host = "localhost"
        self.user = "antonio"
        self.password = "root"
        self.db = "gestione_tamponi"

    def __connect__(self):
        self.con = pymysql.connect(host=self.host,
                                   user=self.user,
                                   password=self.password,
                                   db=self.db,
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

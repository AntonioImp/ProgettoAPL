import sys

sys.path.append('../')
import Database.db_users as db_u


class User:
    """Constructor user class accepts a dictionary with template (first parameter) as:
    {'CF': '',
      'name': '',
      'surname': '',
      'phone': '',
      'mail': '',
      'age': ,
      'CAP': '',
      'city': '',
      'street': '',
      'n_cv': }
      and password as second parameter"""
    
    def __init__(self, user, *password):
        if type(user) == str:
            self.user = db_u.getUser(user)
            if self.user != ():
                self.user = self.user[0]
                self.password = db_u.getPassword(user)[0]["password"]
        else:
            self.user = user
            self.password = password[0]
    
    def getUser(self):
        if self.user != ():
            return self.user
        else:
            return False
    
    def getPassword(self):
        if self.user != ():
            return self.password
        else:
            return False
    
    """ return tuple -> (bool, bool)"""
    def insertUser(self):
        if self.user != ():
            return db_u.insertUser(self.user, self.password)
        else:
            return False
    
    def updateUser(self, user):
        if self.user != ():
            res = db_u.updateUser(self.user["CF"], user)
            if res == True:
                self.user = user
            return res
        else:
            return False
    
    def updatePassword(self, password):
        if self.user != ():
            return db_u.updatePassword(self.user["CF"], password)
        else:
            return False
    
    def deleteUser(self):
        if self.user != ():
            res = db_u.deleteUser(self.user["CF"])
            if res == True:
                self.user = ()
                self.password = ""
            return res
        else:
            return False

    def insertBooking(self, booking):
        if self.user != ():
            return db_u.insertBooking(booking)
        else:
            return False

    def getBooked(self):
        if self.user != ():
            return db_u.getBooked(self.user["CF"])
        else:
            return False
    
    def getBookedComplete(self):
        if self.user != ():
            booked = db_u.getBooked(self.user["CF"])
            execution = db_u.getExecutions()
            res = {}
            print(booked)
            print(execution)
            if execution == ():
                res["complete"] = False
                res["incomplete"] = booked
            elif booked == ():
                res["complete"] = False
                res["incomplete"] = False
            else:
                incomplete = booked[:]
                complete = booked[:]
                for i, b in enumerate(booked):
                    for e in execution:
                        if e["id"] == b["practical_num"]:
                            incomplete.remove(b)
                            complete[i]["time_taken"] = e["time_taken"]
                            complete[i]["result"] = e["result"]
                indexes = []
                for i, c in enumerate(complete):
                    if "result" not in c:
                        indexes.append(i)
                for index in sorted(indexes, reverse=True):
                    del complete[index]
                res["complete"] = complete
                res["incomplete"] = incomplete
            return res
        else:
            return False

    def getExecutions(self):
        if self.user != ():
            return db_u.getExecutions()
        else:
            return False
    
    def deleteBooked(self, practical_num):
        if self.user != ():
            return db_u.deleteBooked(practical_num)
        else:
            return False
    
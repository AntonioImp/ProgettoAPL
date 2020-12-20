import sys

sys.path.append('../')
import Database.db_booking as db_b


class Booking:
    """Constructor booking class accepts a dictionary with template as:
    {
        "CF": "",
        "id": "",
        "CF_M": "",
        "date": "",
        "time": ""
    }"""

    def __init__(self, booking):
        self.booking = ()
        self.name_booking = ""
        self.id_booking = -1

        if type(booking) == int:
            self.id_booking = booking
        elif type(booking) == str:
            self.name_booking = booking
        else:
            self.booking = booking
    
    def insertBooking(self):
        if self.booking != ():
            booked = db_b.getBooked(entity="user", name=self.booking["CF"])
            for b in booked:
                if b["date"] == self.booking["date"]:
                    return -1
            del booked
            return db_b.insertBooking(self.booking)
        else:
            return False

    def getBooked(self, entity):
        if self.name_booking != "":
            return db_b.getBooked(entity, self.name_booking)
        else:
            return False
    
    @staticmethod
    def getAllBooked():
        res = db_b.getAllBooked()
        if res:
            copyRes = [{"date": b["date"], "time_taken": b["time_taken"], "result": b["result"]} for b in res]
            return copyRes
        else:
            return False
    
    def getBookedComplete(self, entity):
        if self.name_booking != "":
            booked = db_b.getBooked(entity, self.name_booking)
            res = {}
            if booked == ():
                res["complete"] = False
                res["incomplete"] = False
            else:
                incomplete = booked[:]
                complete = booked[:]
                indexesI = []
                indexesC = []
                for i, b in enumerate(booked):
                    if b['result'] != None:
                        indexesI.append(i)
                    else:
                        indexesC.append(i)
                for i in sorted(indexesI, reverse=True):
                    del incomplete[i] 
                for i in sorted(indexesC, reverse=True):
                    del complete[i]
                for i in incomplete:
                    del i["time_taken"]
                    del i["result"]
                res["complete"] = complete
                res["incomplete"] = incomplete
            return res
        else:
            return False
    
    def deleteBooked(self, practical_num):
        if self.name_booking != "":
            booked = db_b.getBooked(entity="user", name=self.name_booking)
            for b in booked:
                if b["practical_num"] == practical_num:
                    if b["result"] == None:
                        if db_b.deleteBooked(practical_num):
                            return b
                    return False
            return None
        else:
            return False
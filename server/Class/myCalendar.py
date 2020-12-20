import sys
import datetime
import calendar

sys.path.append('../')
import Database.db_calendar as db_c


class MyCalendar:
    """ L'elemento della classe conterrà l'istanza del medical center a cui si riferisce e un dizionario (calendar)
    composto da giorno di riferimento come key e lista di orari per quel giorno come valori. """

    giorni_settimana = {
        0: "lun",
        1: "mar",
        2: "mer",
        3: "gio",
        4: "ven",
        5: "sab",
        6: "dom"
    }
    
    def __init__(self, medId, day):
        giorno = self.giorni_settimana[calendar.weekday(day.year, day.month, day.day)]
        if(giorno == "dom"):
            raise Exception("Domenica non vengono effettuati tamponi!")
        results = db_c.startCalendar(medId, giorno)
        self.medicalcenter = results[0]
        interval = results[1]
        docs = results[2]
        for doc in docs:
            if doc not in interval:
                interval[doc] = self.medicalcenter["default_interval"]
        
        self.calendar = {}
        for doc, value in interval.items():
            time = self.medicalcenter["start_time"]
            self.calendar[doc] = []
            while time < self.medicalcenter["end_time"]:
                turn = datetime.datetime.strptime(str(time), '%H:%M:%S')
                self.calendar[doc].append(turn.time().replace(second=0))
                time += value
        """for tmp, value in self.calendar.items():
            print(tmp, end=': ')
            for v in value:
                print(str(v), end=', ')
            print("\n--")
        print("----------------")"""

    def updateCalendar(self, day):
        """
        Delete turn already booked
        """
        booked = db_c.getBooked(self.medicalcenter["id"])
        if booked != False and booked != ():
            tmp = booked[:]
            for b in tmp:
                if b["date"] < day or day < b["date"]:
                    booked.remove(b)
            del tmp

            for b in booked:
                turn = datetime.datetime.strptime(str(b["time"]), '%H:%M:%S')
                turn.time().replace(second=0)
                if turn.time() in self.calendar[b["CF_M"]]:
                    self.calendar[b["CF_M"]].remove(turn.time())
    
    def removeBooked(self, turn, doc):
        """
        remove turn in calendar
        """
        dt = datetime.datetime.strptime(str(turn), '%H:%M:%S')
        dt.time().replace(second=0)
        if dt.time() in self.calendar[doc]:
            self.calendar[doc].remove(dt.time())
            return True
        else:
            return False
    
    def reinsertBooked(self, turn, doc):
        """
        reinsert turn in calendar
        """
        dt = datetime.datetime.strptime(str(turn), '%H:%M:%S')
        dt.time().replace(second=0)
        if dt.time() not in self.calendar[doc]:
            self.calendar[doc].append(dt.time())
            self.calendar[doc] = sorted(self.calendar[doc])
            return True
        else:
            return False

    def getCalendar(self):
        """
        return calendar
        """
        if self.calendar != {}:
            return self.calendar
        else:
            return False


if __name__ == "__main__":
    cal = MyCalendar(15, datetime.date(2020,12,14))
    #print(cal.removeBooked('08:30:00', 'C'))
    #print(cal.getCalendar())
    #print(cal.reinsertBooked('08:30:00', 'C'))
    #print(cal.getCalendar())
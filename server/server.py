from flask import Flask, request
from user_server import user_server
from medical_server import medical_server
import Class.medicalcenter as m
import Class.myCalendar as c
import os
import shelve
import datetime

app = Flask(__name__)
app.register_blueprint(user_server, url_prefix = "/user")
app.register_blueprint(medical_server, url_prefix = "/medical")
app.secret_key = os.urandom(16)

class CalendarManager:
    __instance = None
    calendarDict = {}

    @staticmethod
    def getInstance():
        if CalendarManager.__instance == None:
            CalendarManager()
        return CalendarManager.__instance

    def __init__(self):
        if CalendarManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            CalendarManager.__instance = self
            self.currentDay = datetime.date.today()
            self.initCalendarDict()

    def initCalendarDict(self):
        try:
            medical = m.Medicalcenter.getMedicalcenters()
            if medical != False:
                for med in medical:
                    calendar = c.MyCalendar(med["id"], self.currentDay)
                    calendar.updateCalendar(self.currentDay)
                    self.calendarDict[med["id"]] = calendar
                print("CalendarDict creato")
        except Exception as e:
            print(e)
            self.calendarDict = False

    def getCalendarDict(self):
        return self.calendarDict

    def getDate(self):
        return self.currentDay

    def setDate(self, currentDay):
        self.currentDay = currentDay
    
    def removeBooked(self, medId, dt, CF_M):
        return self.calendarDict[medId].removeBooked(turn=dt.time(), doc=CF_M)


""" Metodi di test per il set e get del giorno corrente, passare day in formato YYYY-MM-DD """
@app.route("/setday", methods = ["POST"])
def setDay():
    try:
        date_f = '%Y-%m-%d'
        dt = datetime.datetime.strptime(request.json["day"], date_f)
    except:
        return "-1" #->"Datetime format error"
    manager = CalendarManager.getInstance()
    manager.setDate(dt.date())
    manager.initCalendarDict()
    with shelve.open('archive') as archive:
        archive['manager'] = manager
    return "0" #->"Giorno aggiornato"

@app.route("/getday", methods = ["POST"])
def getDay():
    return CalendarManager.getInstance().getDate()


if __name__ == "__main__":
    manager = CalendarManager.getInstance()
    with shelve.open('archive') as archive:
        archive['manager'] = manager
    app.run()
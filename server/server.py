from flask import Flask, request
from user_server import user_server
from medical_server import medical_server
from dotenv import load_dotenv
from os import getenv, urandom
from rpy2 import robjects as ro
import Class.medicalcenter as m
import Class.myCalendar as c
import Class.booking as b
import Class.doc as d
import shelve
import datetime

load_dotenv(dotenv_path='.env')
app = Flask(__name__)
app.debug = getenv("DEBUG") == "True"
app.register_blueprint(user_server, url_prefix = "/user")
app.register_blueprint(medical_server, url_prefix = "/medical")
app.secret_key = urandom(16)

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
            self.calendarDict = False
            medical = m.Medicalcenter.getMedicalcenters()
            if medical != False:
                self.calendarDict = {}
                for med in medical:
                    calendar = c.MyCalendar(med["id"], self.currentDay)
                    calendar.updateCalendar(self.currentDay)
                    self.calendarDict[med["id"]] = calendar
                print("CalendarDict creato")
        except Exception as e:
            print("Error:", e)
            self.calendarDict = False

    def getCalendarDict(self):
        return self.calendarDict

    def getDate(self):
        return self.currentDay

    def setDate(self, currentDay):
        self.currentDay = currentDay
    
    def removeBooked(self, medId, dt, CF_M):
        return self.calendarDict[medId].removeBooked(turn=dt.time(), doc=CF_M)
    
    def reinsertBooked(self, medId, dt, CF_M):
        return self.calendarDict[medId].reinsertBooked(turn=dt.time(), doc=CF_M)


""" Metodi di test per il set e get del giorno corrente, passare day in formato YYYY-MM-DD """
@app.route("/setday", methods = ["POST"])
def setDay():
    try:
        date_f = '%Y-%m-%d'
        dt = datetime.datetime.strptime(request.json["day"], date_f)
    except:
        return "-1" #->"Datetime format error"

    ro.r.source("script.R")
    
    manager = CalendarManager.getInstance()
    manager.setDate(dt.date())
    manager.initCalendarDict()
    flag = None
    with shelve.open('archive') as archive:
        archive['manager'] = manager
        if 'flag' in archive:
            flag = archive['flag']
            del archive['flag']
        archive.close()
    if flag != None:
        for f in flag:
            d.Doc(f[0]).dismissDoc(f[1], manager.getDate()) #->"Elimino dottori che hanno completato la prenotazione e dovevano essere dimessi"

    return "0" #->"Giorno aggiornato"

@app.route("/getday")
def getDay():
    return str(CalendarManager.getInstance().getDate())

@app.route("/getallbooked")
def getAllBooked():
    res = b.Booking.getAllBooked()
    json = {}
    json["booked"] = []
    for r in res:
        r["time_taken"] = str(r["time_taken"])
        r["date"] = str(r["date"])
        json["booked"] += [r,]
    return json

@app.route('/shutdown', methods=['GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

if __name__ == "__main__":
    manager = CalendarManager.getInstance()
    with shelve.open('archive') as archive:
        archive['manager'] = manager
        # for data in archive.keys():
        #     print( data , archive[ data ])
        archive.close()
    app.run()
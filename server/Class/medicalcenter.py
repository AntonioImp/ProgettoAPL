import sys

sys.path.append('../')
import Database.db_medicalcenter as db_m


class Medicalcenter:
    """Constructor medicalcenter class accepts a dictionary with template (first parameter) as:
    {"p_IVA": "",
    "phone": "",
    "mail": "",
    "CAP": "",
    "city": "",
    "street": "",
    "n_cv": }
    and password as second parameter"""
    
    def __init__(self, med, *password):
        if type(med) == int:
            self.medicalcenter = db_m.getMedicalcenter(med)
            if self.medicalcenter != ():
                self.medicalcenter = self.medicalcenter[0]
                self.password = db_m.getPassword(med)[0]["password"]
        else:
            self.medicalcenter = med
            self.password = password[0]
            
    def getMedicalcenter(self):
        if self.medicalcenter != ():
            return self.medicalcenter
        else:
            return False

    @staticmethod
    def getMedicalcenters():
        return db_m.getMedicalcenters()
    
    def getPassword(self):
        if self.medicalcenter != ():
            return self.password
        else:
            return False
    
    def getBooked(self):
        if self.medicalcenter != ():
            return db_m.getBooked(self.medicalcenter["id"])
        else:
            return False

    """ return tuple -> (bool, bool, medical center id)"""
    def insertMedicalcenter(self):
        if self.medicalcenter != ():
            return db_m.insertMedicalcenter(self.medicalcenter, self.password)
        else:
            return False
        
    def updateMedicalcenter(self, med):
        if self.medicalcenter != ():
            res = db_m.updateMedicalcenter(self.medicalcenter["id"], med)
            if res == True:
                self.medicalcenter = med
            return res
        else:
            return False
        
    def updatePassword(self, password):
        if self.medicalcenter != ():
            return db_m.updatePassword(self.medicalcenter["id"], password)
        else:
            return False
    
    def updateTiming(self, start_time, end_time, default_interval):
        if self.medicalcenter != ():
            res = db_m.updateTiming(self.medicalcenter["id"], start_time, end_time, default_interval)
            if res:
                self.medicalcenter["start_time"] = start_time
                self.medicalcenter["end_time"] = end_time
                self.medicalcenter["default_interval"] = default_interval
            return res
        else:
            return False

        
    def deleteMedicalcenter(self):
        if self.medicalcenter != ():
            res = db_m.deleteMedicalcenter(self.medicalcenter["id"])
            if res == True:
                self.medicalcenter = ()
                self.password = ""
            return res
        else:
            return False
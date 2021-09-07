import sys

sys.path.append('../')
import Database.db_doc as db_d

class Doc:
    """Constructor doc class accepts a dictionary with template as:
    {'CF': '',
      'name': '',
      'surname': '',
      'phone': '',
      'mail': ''}"""
    
    def __init__(self, doc):
        if type(doc) == str:
            self.doc = db_d.getDoc(doc)
            if self.doc != ():
                self.doc = self.doc[0]
        else:
            self.doc = doc
            
    def getDoc(self):
        if self.doc != ():
            return self.doc
        else:
            return False
    
    @staticmethod
    def getDocAssignment(medId):
        """ Retrieve the doctors (CF and day) who work for medId and
            the doctors registered to the system. Once the list of
            doctors has been created, it takes care of grouping the
            working days for each doctor. """

        lis, docs = db_d.getDocAssignment(medId)
        union = []
        for doc in docs:
            for l in lis:
                if l["CF"] == doc["CF"]:
                    tmp = dict(doc.items())
                    tmp.update(l)
                    union.append(tmp)
        del lis, docs
        copyRes = [r.copy() for r in union] #create copy
        for cr in copyRes:  #delete day by each copy
            del cr["day"]
        uniqueCopyRes = []
        for x in copyRes:   #insert each doc only one times
            if x not in uniqueCopyRes:
                uniqueCopyRes.append(x)
        del copyRes
        for cr in uniqueCopyRes:
            cr["avarage_time"] = str(cr["avarage_time"])
            cr["day"] = []
            for d in union:     #for each doc, insert list of working day
                if cr["CF"] == d["CF"]:
                    cr["day"].append(d["day"])
        return uniqueCopyRes
        
    """ return tuple -> (bool insert docs, bool insert docs_list)
        or (bool insert docs_list,) if doc is already in docs table"""
    def insertDoc(self, medId, days):
        if self.doc != ():
            return db_d.insertDoc(medId, self.doc, days)
        else:
            return False
        
    def updateDoc(self, doc):
        if self.doc != ():
            res = db_d.updateDoc(self.doc["CF"], doc)
            if res == True:
                self.doc = doc
            return res
        else:
            return False
        
    def dismissDoc(self, medId, day):
        if self.doc != ():
            res = db_d.controlDismissDoc(self.doc["CF"])
            if res != ():
                for b in res:
                    if b["date"] == day:
                        return "-1" #->"Dottore impegnato in prenotazioni"
            return db_d.dismissDoc(self.doc["CF"], medId)
        else:
            return False
        
    def deleteDoc(self):
        if self.doc != ():
            return db_d.deleteDoc(self.doc["CF"])
        else:
            return False

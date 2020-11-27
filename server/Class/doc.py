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
    def getDocAssignment(*data):
        return db_d.getDocAssignment(data)
        
    """ return tuple -> (bool insert docs, bool insert docs_list)
        or (bool insert docs_list,) if doc is already in docs table"""
    def insertDoc(self, medId):
        if self.doc != ():
            return db_d.insertDoc(medId, self.doc)
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
        
    def dismissDoc(self, medId):
        if self.doc != ():
            return db_d.dismissDoc(self.doc["CF"], medId)
        else:
            return False
        
    def deleteDoc(self):
        if self.doc != ():
            return db_d.deleteDoc(self.doc["CF"])
        else:
            return False

import sys

sys.path.append('../')
import Database.db_calendar as db_c


class Calendar:
    """ L'elemento della classe conterrà l'istanza del medical center a cui si riferisce e un dizionario
    composto da giorno di riferimento come key e lista di orari per quel giorno come valori """

    def __init__(self, medId):
        results = db_c.startCalendar(medId)
        self.medicalcenter = results[0]
        self.doc_timing = results[1]

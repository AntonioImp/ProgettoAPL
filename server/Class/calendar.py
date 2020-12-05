import sys

sys.path.append('../')
import Database.db_calendar as db_c


class Calendar:
    """ L'elemento della classe conterrà l'istanza del medical center a cui si riferisce e un dizionario
    composto da giorno di riferimento come key e lista di orari per quel giorno come valori.
    Sono inoltre presenti il campo today che contiene la lista degli orari per il dottore rispetto
    all'andamento avuto dallo stesso nei giorni precedenti """

    def __init__(self, medId):
        results = db_c.startCalendar(medId)
        self.medicalcenter = results[0]
        doc_timing = sorted(results[1], key=lambda l: l["date"], reverse=True)
        docs = results[2]

        interval = {}
        for doc in docs:
            for d in doc_timing:
                if doc == d["CF"]:
                    interval[doc] = d["avarage_time"]
                    break
        
        for doc in docs:
            if doc not in interval:
                interval[doc] = self.medicalcenter["default_interval"]
        
        self.today = []
        for doc, value in interval.items():
            time_scan = {}
            time = self.medicalcenter["start_time"]
            time_scan[doc] = []
            while time < self.medicalcenter["end_time"]:
                time_scan[doc].append(time)
                time += value
            self.today.append(time_scan)

        """for tmp, value in time_scan.items():
            print(tmp, end=': ')
            for v in value:
                print(str(v), end=', ')
            print("\n--")
        print("----------------")
        for tmp in self.today:
            for tmp2, value in tmp.items():
                print(tmp2, end=': ')
                for v in value:
                    print(str(v), end=', ')
                print("\n--")"""


if __name__ == "__main__":
    Calendar(15)
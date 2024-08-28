import os
import shelve
import Data.generalSmallFuncModule as GSFMod

class DataBank:
    def __init__(self, directory, filename):
        self.filepath = os.path.join(directory, filename)

    def loadFlags(self):
        with shelve.open(self.filepath) as db:
            try:
                listOfFlags = []
                for x in db:
                    if x != "flags":
                        listOfFlags.append(x)
                return listOfFlags
            except:
                return False

    def save_list(self, flag, data):
        with shelve.open(self.filepath, writeback=True) as db:
            db[flag] = data
            flags = db.get("flags", {})
            flags[flag] = len(data)
            db["flags"] = flags

    def load_list(self, flag):
        with shelve.open(self.filepath) as db:
            try:
                return db[flag]
            except:
                return False
    
    def delete_list(self, flag):
        with shelve.open(self.filepath, writeback=True) as db:
            if flag in db:
                del db[flag]
                flags = db.get("flags", {})
                if flag in flags:
                    del flags[flag]
                    db["flags"] = flags
    
    def delete_data_bank(file):
        if os.path.exists(dt_file1):
            os.remove(dt_file1)
            os.remove(dt_file2)
            os.remove(dt_file3)
            GSFMod.bankKillScreen()
        else:
            print("\u25BA    Data bank file not found.  \u25C4")


DB = os.path.join(os.path.dirname(__file__), "dataBank")
data_bank = DataBank(DB, "Orçamentos.db")

dt_file1 = os.path.join(os.path.dirname(__file__), "dataBank", 'Orçamentos.db.bak')
dt_file2 = os.path.join(os.path.dirname(__file__), "dataBank", 'Orçamentos.db.dat')
dt_file3 = os.path.join(os.path.dirname(__file__), "dataBank", 'Orçamentos.db.dir')

import pandas as pd
import wbdata

class wbank():
    def __init__(self, location):
        self.location = location
        
    def API_to_db(self, indicator):
        self.indicator = indicator
        data = wbdata.get_dataframe(self.indicator, country=self.location)
        data.reset_index(level=[0,1], inplace = True)
        return data

    def latest(self, db):
        self.db = db
        latest = db.date.tolist()[0]
        return latest

    def db_to_date(self, db, econ_ind, latest):
        self.db = db
        self.econ_ind = econ_ind
        self.latest = latest
        latest_uk = round(self.db.loc[(self.db["country"] == "United Kingdom") & (self.db["date"] == self.latest)])
        latest_uk_x= latest_uk.iloc[0][self.econ_ind]  
        return latest_uk_x        

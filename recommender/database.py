import pandas as pd
import numpy as np

class Database(object):
    def __init__(self, place):
        self.data = pd.read_csv('data/places.csv', index_col=0)
        # print(self._data.loc[plus_code])
        self.search(place)

    def search(self, place):
        print('Performing Database search ...')
        codes = self.data['plus_code'].values
        for index in range(len(codes)):
            if str(codes[index]) == place.plus_code:
                print('Woo hoo ! Found !')
                place.in_db = True
                place.subtype = self.data.iloc[index].loc['subtype']
                place.covidprec[0] = self.data.iloc[index].loc['masks']
                place.covidprec[1] = self.data.iloc[index].loc['limited_entry']
                place.covidprec[2] = self.data.iloc[index].loc['early_close']
                place.covidprec[3] = self.data.iloc[index].loc['has_early']
                place.covidprec[4] = self.data.iloc[index].loc['early_hours']
                place.covidprec[5] = self.data.iloc[index].loc['delivery']
                place.has_pt = place.covidprec[0] = self.data.iloc[index].loc['has_pt']
                place.has_live = place.covidprec[0] = self.data.iloc[index].loc['has_live']

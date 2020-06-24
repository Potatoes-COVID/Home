import pandas as pd
import numpy as np

class Database(object):
    def __init__(self, place):
        self._data = pd.read_csv('data/places.csv', index_col=0)
        # print(self._data.loc[lat_lng])
        self.search(place)

    def search(self, place):
        print('Performing Database search ...')

        if place.plus_code in self._data.values:
            place.in_db = True
            place.subtype = self._data.loc[lat_lng].iloc[1]
            place.covidprec[0] = self._data.loc[lat_lng].iloc[2]
            place.covidprec[1] = self._data.loc[lat_lng].iloc[3]
            place.covidprec[2] = self._data.loc[lat_lng].iloc[4]
            place.covidprec[3] = self._data.loc[lat_lng].iloc[5]
            place.covidprec[4]= self._data.loc[lat_lng].iloc[6]
            place.covidprec[5] = self._data.loc[lat_lng].iloc[7]
            place.has_pt = self._data.loc[lat_lng].iloc[8]
            place.has_live = self._data.loc[lat_lng].iloc[9]
            print('Woo hoo ! Found !')

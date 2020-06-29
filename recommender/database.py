import pandas as pd

# Class for opening the database csv file and searching it
class Database(object):
    def __init__(self, place):
        self.data = pd.read_csv('data/places.csv', index_col=0)
        self.search(place)

    def search(self, place):
        print('Performing Database search ...')
        codes = self.data['plus_code'].values
        for index in range(len(codes)):
            if str(codes[index]) == place.plus_code:
                print('Woo hoo ! Found !')
                place.in_db = True
                place.subtype = self.data.at[index, 'subtype']
                place.covidprec[0] = self.data.at[index, 'masks']
                place.covidprec[1] = self.data.at[index, 'limited_entry']
                place.covidprec[2] = self.data.at[index, 'early_close']
                place.covidprec[3] = self.data.at[index, 'has_early']
                place.covidprec[4] = self.data.at[index, 'early_hours']
                place.covidprec[5] = self.data.at[index, 'delivery']
                place.has_pt = self.data.at[index, 'has_pt']
                place.has_live = self.data.at[index, 'has_live']

import pandas as pd
import numpy as np

class Database(object):
    def __init__(self, plus_code):
        self._data = pd.read_csv('data/places.csv', index_col=0)
        print(self._data['plus_code'][0])
        if plus_code == self._data['plus_code'][0]:
            print('suuuucka')
        return



#    print(get_data())

# for (index, row) in places.iterrows():
#    print("Populating " + str(index))
#    moments = get_place_popular_moments(row.place_id)
#    if moments != None:
#        self.data.at[index, 'monday'] = moments[0]['data']
#        self.data.at[index, 'tuesday'] = moments[1]['data']
#        self.data.at[index, 'wednesday'] = moments[2]['data']
#        self.data.at[index, 'thursday'] = moments[3]['data']
#        self.data.at[index, 'friday'] = moments[4]['data']
#        self.data.at[index, 'saturday'] = moments[5]['data']
#        self.data.at[index, 'sunday'] = moments[6]['data']

#places.to_csv('data/places_with_moments.csv')
#print(self.data)

import pandas as pd

class Database:
    def _init_(self):
        self.places = pd.read_csv('data/places.csv', index_col=0)
        self.last_index = 0
        self.results = []
        return

    def search(s):
        results = []
        for (index, row) in places.iterrows():
            name = row.place_name
            self.last_index = index
            if name == s:
                results[0] = true
                results[1] = row.masks
                results[2] = row.limited_entry
                results[3] = row.early_close
                results[4] = row.has_pt
                results[5] = row.has_live
                update_results(results)
        return self.results

    def add(place, has_pt, has_live):
        self.places.at[self.last_index+1, 'place_name'] = place
        self.places.at[self.last_index+1, 'has_pt'] = has_pt
        self.places.at[self.last_index+1, 'has_live'] = has_live
        return
        
    def update_results(r):
        self.results[0] = r[0]
        if r[1] == 1:
            self.results[1] = true
        else:
            self.results[1] = false

        if r[2] == 1:
            self.results[2] = true
        else:
            self.results[2] = false

        if r[3] == 1:
            self.results[3] = true
        else:
            self.results[3] = false

        if r[4] == 1:
            self.results[4] = true
        else:
            self.results[4] = false

        if r[5] == 1:
            self.results[5] = true
        else:
            self.results[5] = false
        return

    def add_place(place):

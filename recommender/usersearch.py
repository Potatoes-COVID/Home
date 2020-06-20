
import json
import urllib.request as url_req
import time
import place
import pandas as pd
from config.api import APIKey

class UserSearch:
    def _init_(self, results):
            self.name = results[0]['name']
            self.type = results[0]['types'][0]
            self.places = []
            self.recs = []
            create_places(results)
            print("Name : %s", self.name)
            return

    # for each place in places
    # if we have 5 recs, end
    # if we have created 5 places, & we have at least 2 places in our recs, end
    # else, create a place object, check the database for it
    # if it has a live value, add it to our recs array, else add it to our places
    def create_places(self, places):
        for p in range(places):
            num_recs = self.recs.length()
            num_places = self.places.length()
            if num_recs == 5: break
            else if num_places == 5 && num_recs > 1: break
            else:
                place = Place(p)
                if place.has_live:
                    self.recs += place
                else:
                    self.places += place
        sort_recs()

    # if num_recs < 5 [we have < 5 places with live times], add places from
    # our places array to our recs. sort the places by their rank, first !
    # then sort the recs array
    def sort_recs(self):
        num_recs = self.recs.length()
        if num_recs < 5:
            sorted(self.places, key=lambda place: place.rank)
            max = 4
            for index in range(max):
                self.recs += self.places[index]
                num_recs += 1
                if num_recs == 5:
                    break
        sorted(self.recs, key=lambda place: place.rank)

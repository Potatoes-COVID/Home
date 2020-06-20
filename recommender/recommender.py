import json
import urllib.request as url_req
import time
import pandas as pd
import usersearch
import nearbysearch
from config.api import apikey

# create recs --> recommender = Recommender(search)
# target_search_recommendations = recommender.user_search_recs
# nearby_search_recommendations = recommender.nearby_search_recs
class Recommender:
    # loads the JSON & get the results returned from the search
    # send them to UserSearch for handling, then get the type
    # of the initial search, and the users approx location by
    # using the first place in the results array and send it to
    # NearbySearch for handling
    def _init_(search):
        self.srch = json.loads(search)
        self.usr = self.srch['results']
        self.user_search_recs = UserSearch(usr)

        self.search_type = self.usr[0]['types'][0]
        self.loc = get_location()
        self.nearby_search_recs = NearbySearch(self.loc, self.search_type)
        return

    def get_location(self):
        lat = self.usr[0]['geometry']['location']['lat']
        lng = self.usr[0]['geometry']['location']['lng']
        return str(lat) + ',' + str(lng)

import json
import urllib.request as url_req
import time
import place as p
from config.api import apikey

class NearbySearch(object):
    def __init__(self, location, type, os_name):
        self.api_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
        self.apikey = apikey
        self.loc = location
        self.type = type
        self.radius = 5000                                  # meters : ~3.1 miles
        self.recs = []
        self.places = []
        self.os_name = os_name
        nsr = self.search_nearby()
        self.create_places(nsr)
        print("Type: ", self.type)
        return

    # method for requesting the api's url
    def request_api(self, url):
        response = url_req.urlopen(url)
        json_raw = response.read()
        json_data = json.loads(json_raw)
        return json_data

    # generate the url needed to do a nearby search
    # perform the search & returns the results
    def search_nearby(self):
        self.search_url = ('%s'
            '?location=%s'
            '&radius=%s'
            '&type=%s'
            '&key=%s') % (self.api_url, self.loc, self.radius, self.type, self.apikey)

        results = []
        api_response = self.request_api(self.search_url)
        results = results + api_response['results']

        time.sleep(1)
        return results


    # for each place in places
    # if we have 5 recs, end
    # if we have created 5 places, & we have at least 2 places in our recs, end
    # else, create a place object, check the database for it
    # if it has a live value, add it to our recs array, else add it to our places
    def create_places(self, places):
        for pl in range(len(places)):
            num_recs = len(self.recs)
            num_places = len(self.places)
            if num_recs == 5: break
            if num_places == 5:
                if num_recs > 1: break
            else:
            #    if p['name'] != self.os_name:
                place = p.Place(places[pl])
                if place.has_live:
                    self.recs.append(place)
                else:
                    self.places.append(place)
        self.sort_recs()

    # if num_recs < 5 [we have < 5 places with live times], add places from
    # our places array to our recs. sort the places by their rank, first
    # then sort the recs array
    def sort_recs(self):
        num_recs = len(self.recs)
        if num_recs < 5:
            sorted(self.places, key=lambda place: place.rank)
            max = 4
            for index in range(max):
                self.recs.append(self.places[index])
                num_recs += 1
                if num_recs == 5:
                    break
        sorted(self.recs, key=lambda place: place.rank)

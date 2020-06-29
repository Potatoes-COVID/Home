from config.api import apikey
import livepopulartimes
import database as db
from datetime import datetime

class Place(object):
    def __init__(self, place):
        self.map_url = 'https://www.google.com/maps/search/'
        self.key = apikey

        self.name = place['name']
        self.place_id = place['place_id']
        self.plus_code = place['plus_code']['compound_code']
        self.loc = self.get_location(place)

        self.in_db = False
        self.subtype = ''
        self.covidprec = [-1,-1,-1,-1,[],-1]     # masks, lim_ent, early_close, has_early, early_hours, delivery
        self.has_pt = False
        self.has_live = False
        self.live = 0
        self.url = ''

        db.Database(self)
        if self.has_live:
            self.url = self.get_url()
            self.pop_times = self.get_place_popular_moments()
            self.get_live_time()
        self.calc_rank()
        self.json = self.place_to_JSON()

    def get_location(self, place):
        lat = place['geometry']['location']['lat']
        lng = place['geometry']['location']['lng']
        return str(lat) + ',' + str(lng)

    # url for hyper-linking results?
    def get_url(self):
        return ('%s'
                '?api=%s'
                '&query=%s'
                '&query_place_id=%s') % (self.map_url, self.key, self.loc, self.place_id)
    def get_place_popular_moments(self):
        popular_moments = livepopulartimes.get_populartimes_by_PlaceID(self.key, self.place_id)
        if 'populartimes' in popular_moments:
            return popular_moments['populartimes']
        else:
            return None

    def get_live_time(self):
        day_num = datetime.today().weekday()
        hour = datetime.now().hour
        day_pt = self.pop_times[day_num]['data']
        self.live = day_pt[hour]

    # Needs subtype consideration
    def calc_rank(self):
        self.rank = 0
        for i in range(len(self.covidprec)):
            if i != 2:
                if self.covidprec[i] == 1:
                    self.rank += 1
        if self.has_pt:
            self.rank += 1
            if self.has_live:
                self.calc_live_rank()
        print("Rank: ", self.rank)

    def calc_live_rank(self):
        if 0 <= self.live <= 25:
            self.rank += 20
        if 26 <= self.live <= 50:
            self.rank += 15
        if 51 <= self.live <= 75:
            self.rank += 10
        if 76 <= self.live <= 90:
            self.rank += 5

    def place_to_JSON(self):
        place = {
            "name" : str(self.name),
            "live" : str(self.live),
            "rank" : str(self.rank),
            "place_id" : str(self.place_id),
            "covidprec" : str(self.covidprec),
            "place_url" : str(self.url),
        }
        return place

    # in place for testing
    def print_place(self):
        print('Name : ' + self.name)
        print('Place ID: ' + self.place_id)
        print('Plus Code : ' + str(self.plus_code))
        print('Found? ' + str(self.in_db))
        return

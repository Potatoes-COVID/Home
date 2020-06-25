from config.api import apikey
import populartimes
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

        db.Database(self)
        if self.has_live:
            # self.get_url()
            self.pop_times = self.get_place_popular_moments()
            self.get_live_time()
            # self.live = WebScraper(self.url)
        self.calc_rank()
        #self.print_place()

    def get_location(self, place):
        lat = place['geometry']['location']['lat']
        lng = place['geometry']['location']['lng']
        return str(lat) + ',' + str(lng)

    # url for WebScraper
    def get_url(self):
        return ('%s'
                '?api=%s'
                '&query=%s'
                '&query_place_id=%s') % (self.map_url, self.key, self.loc, self.place_id)

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

    def get_place_popular_moments(self):
        popular_moments = populartimes.get_id(self.key, self.place_id)
        if 'populartimes' in popular_moments:
            return popular_moments['populartimes']
        else:
            return None

    def get_live_time(self):
        day_num = datetime.today().weekday()
        hour = datetime.now().hour
        day_pt = self.pop_times[day_num]['data']
        self.live = day_pt[hour]

    # in place for testing
    def print_place(self):
        print('Name : ' + self.name)
        print('Place ID: ' + self.place_id)
        print('Plus Code : ' + str(self.plus_code))
        print('Found? ' + str(self.in_db))
        return

from config.api import apikey
import database as db

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
        self.covidprec = []     # subtype, masks, lim_ent, early_close, has_early, early_hours, delivery
        self.has_pt = False
        self.has_live = False

        db.Database(self)
        if self.has_live:
            self.get_url()
            # WebScraper(self.url)
        self.rank = self.get_rank()

        self.print_place()

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

    # WIP
    def get_rank(self):
        rank = 0
        return rank

    # in place for eventual testing
    def print_place(self):
        print('Name : ' + self.name)
        print('Place ID: ' + self.place_id)
        print('Plus Code : ' + str(self.plus_code))
        return

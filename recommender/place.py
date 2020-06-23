from config.api import apikey
# import database

class Place:
    def _init_(self, place):
        self.map_url = 'https://www.google.com/maps/search/'
        self.key = apikey

        self.name = place['name']
        self.place_id = place['place_id']
        self.plus_code = place['plus_code']
        self.loc = get_location(place)

        self.covidprec = []
        self.has_pt = false
        seelf.has_live = false

        query_db()
        self.rank = get_rank()

        print_place()
        return

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

    # WIP -- STILL NEED TO WRITE DATABASE
    # CODE COULD CHANGE
    def query_db(self):
        db = Databse()
        results = db.search(self.plus_code)
        found = true, subtype, covid [5], pt, lt
        if results[0]:
            self.subtype = results[1]
            for index in results:
                if index >= 2 && index < 8:
                    self.covidprec = self.covidprec + results[index]
            if results[7]:
                # pt
                self.has_pt = true
                if results[8]:
                    self.has_live = true
                self.url = get_url()
                self.pop_times = WebScraper(self.url, self.has_live)
                return true
        else:
            self.url = get_url()
            self.has_live = true                              # we're not sure so we want it to check for us
            self.pop_times = WebScraper(self.url, self.has_live)
            db.add(self)
        return false

        # WIP
        def get_rank(self):
            rank = 0
            return rank

        # in place for eventual testing
        def print_place(self):
            print('Name : ' + self.name)
            print('Place ID: ' + self.place_id)
            print('Plus Code : ' + self.plus_code)

class Place:
    # constructor; parses the Google place type to create our own
    def _init_(self, place, os):
        api_url = "https://www.google.com/maps/search/?api="
        apikey = 'AIzaSyBMZ6xYlzyjMEZTWiXWF7F6KlvOI-rvWm0'

        self.name = place.name
        self.os = os                                        # whether or not this is an original search place
        self.id = place.place_id
        self.loc = place.geometry.location.toUrlValue()     # worried this is for javascript lol; LOOK INTO
        self.has_pt = false                                 # whether or not it has popular times data; to be determined from DB
        self.has_live = false                               # whether or not it has live times data; to be determined from DB
        self.live = 0                                       # live value
        self.covidprec = [false, false, false]              # [MASKS: BOOL, LIMITED_ENTRY: BOOL, EARLY_CLOSE: BOOL]
        self.poptimes = []                                  
        self.rank = 0                                       # to be added to as place parameters are determined
        self.db = Databse()
        self.url = ('s'
                    '?api=%s'
                    '&query=%s'
                    '&query_place_id=%s') % (api_url, apikey, loc, id)

        found = get_database_info()
        if !found:
            get_pop_times()
            db.add(self.name, self.has_pt, self.has_live)
        else:
            if self.has_pt:
                get_pop_times()
        return

    # calls the Databse to get the covid precautions for stores of that name,
    # as well as if they have popular times data available. will return
    # true or false depending on if the place was found
    def get_database_info():
        results = self.db.search(name)
        if results[0]:                                      # found - bool
            self.covidprec[0] = results[1]                  # masks - bool
            if self.covidprec[0]:
                self.rank += 1
            self.covidprec[1] = results[2]                  # limited_entry - bool
            if self.covidprec[1]:
                self.rank += 1
            self.covidprec[2] = results[3]                  # early_close - bool
            if self.covidprec[2]:
                self.rank += 1
            self.has_pt = results[4]
            self.has_live = results[5]
            return true
        return false

    # calls the WebScraper to search for the desired place to scrub its
    # popular times & live times, if available (updates values of has_pt
    # & has_live if they are)
    def get_pop_times():
        ws = WebScraper()
        results = ws.search(self.url)                       # [%: INT, LIVE: BOOL]
        if results[0][0] != -1:
            self.has_pt = true
            self.rank += 1
            for r in range(results):
                self.poptimes[r] = r[0]
                if r[1]:
                    self.has_live = true
                    self.live = r[0] * 0.01
                    self.rank += (1-self.live)                  #
        return

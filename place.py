class Place:
    def _init_(self, place, os):
        api_url = "https://www.google.com/maps/search/?api="
        apikey = 'AIzaSyBMZ6xYlzyjMEZTWiXWF7F6KlvOI-rvWm0'

        self.name = place.name
        self.os = os
        self.id = place.place_id
        self.loc = place.geometry.location.toUrlValue()
        self.has_pt = false
        self.has_live = false
        self.live = 0
        self.covidprec = [false, false, false]          # [MASKS: BOOL, LIMITED_ENTRY: BOOL, EARLY_CLOSE: BOOL]
        self.poptimes = []
        self.rank = 0
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

        calculate_rank()
        return

    def get_database_info():
        db = Databse()
        results = db.search(name)
        if results[0]:
            self.covidprec[0] = results[1]
            self.covidprec[1] = results[2]
            self.covidprec[2] = results[3]
            self.has_pt = results[4]
            self.has_live = results[5]
            return true
        return false

    def get_pop_times():
        ws = WebScraper()
        results = ws.search(self.url)       # [%: INT, LIVE: BOOL]
        for r in range(results):
            self.poptimes[r] = r[0]
            if r[1]:
                self.has_live = true
                self.live = r[0] * 0.01
        return

    def get_live_rank():
        for t in range(self.poptimes):
            if t[1]:
                r = t[0] * 0.01      # if rank live is already sent as a decimal, * 0.01 could be removed
                self.rank -= r            # if it has a live, we added 1. Now we'll subtract the % of people from that 1.
        return

    def calculate_rank():
        if self.covidprec[0]:
            self.rank += 1
        if self.covidprec[1]:
            self.rank += 1
        if self.covidprec[2]:
            self.rank += 1
        if self.has_pt:
            self.rank += 1
            if self.has_live:
                self.rank += (1-self.live)
        return

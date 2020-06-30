import place as p
import nearbysearch as ns

class UserSearch(object):
    def __init__(self, results):
            self.name = results[0]['name']
            self.type = results[0]['types'][0]
            self.places = []
            self.recs = []
            self.subtype = self.places[0].subtype
            self.loc = self.places[0].loc
            self.nsr = ns.NearbySearch(self.loc, self.type, self.subtype, self.name)
            self.create_places(results)

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
                place = p.Place(places[pl], self.subtype, self.name)
                if place.has_live:
                    self.recs.append(place.json)
                else:
                    self.places.append(place.json)

        self.sort_recs()

    # if num_recs < 5 [we have < 5 places with live times], add places from
    # our places array to our recs. sort the places by their rank, first !
    # then sort the recs array
    def sort_recs(self):
        num_recs = len(self.recs)
        if num_recs < 5:
            sorted(self.places, key=lambda place: place['rank'])
            max = 4
            for index in range(max):
                self.recs.append(self.places[index])
                num_recs += 1
                if num_recs == 5: break
        sorted(self.recs, key=lambda place: place['rank'])

import usersearch
import nearbysearch

# create recs --> recommender = Recommender(search)
# target_search_recommendations = recommender.user_search_recs
# nearby_search_recommendations = recommender.nearby_search_recs

# loads the JSON & get the results returned from the search
# send them to UserSearch for handling, then get the type
# of the initial search, and the users approx location by
# using the first place in the results array and send it to
# NearbySearch for handling
def recommender(search):
    srch = json.loads(search)
    usr = self.srch['results']
    user_search_recs = UserSearch(usr)

    search_type = self.usr[0]['types'][0]
    loc = self.get_location()
    nearby_search_recs = NearbySearch(loc, search_type, usr[0]['name'])
    return [user_search_recs, nearby_search_recs]

def get_location(self):
    lat = self.usr[0]['geometry']['location']['lat']
    lng = self.usr[0]['geometry']['location']['lng']
    return str(lat) + ',' + str(lng)

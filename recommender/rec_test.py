import json
import usersearch as us
import nearbysearch as ns

# create recs --> recommender = Recommender(search)
# target_search_recommendations = recommender.user_search_recs
# nearby_search_recommendations = recommender.nearby_search_recs

# loads the JSON & get the results returned from the search
# send them to UserSearch for handling, then get the type
# of the initial search, and the users approx location by
# using the first place in the results array and send it to
# NearbySearch for handling
def recommender(search):
    #srch = json.loads(search)
    #usr = srch['results']
    #user_search_recs = us.UserSearch(usr)

    search_type = 'supermarket' #usr[0]['types'][0]
    # loc = get_location()
    loc = '34.2410079,-118.5401147'
    nearby_search_recs = ns.NearbySearch(loc, search_type, 'target')#usr[0]['name'])

    recs = get_json(nearby_search_recs.recs)
    with open("data/data_file_rec.json", "w") as write_file:
        json.dump(recs, write_file)

def get_location():
    lat = self.usr[0]['geometry']['location']['lat']
    lng = self.usr[0]['geometry']['location']['lng']
    return str(lat) + ',' + str(lng)

def get_json(nearby_search_recs):
    recs = {
        # "usersearch" : user_search_recs,
        "nearbysearch" : nearby_search_recs
    }
    return recs

with open("data/data_file_read.json") as read_file:
    data = json.load(read_file)

recommender(data)

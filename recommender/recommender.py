import json
import usersearch as us

# create recs --> recommender = Recommender(search)
# target_search_recommendations = recommender.user_search_recs
# nearby_search_recommendations = recommender.nearby_search_recs

# loads the JSON & get the results returned from the search
# send them to UserSearch for handling
# updates the JSON file with the new recommendation
def recommender():
    with open("map_data/data_file_read.json") as read_file:
        srch = json.load(read_file)
        
    usr = srch['results']
    recs = us.UserSearch(usr)
    user_search_recs = recs.recs
    nearby_search_recs = recs.nsr

    j_recs = {
        "usersearch" : user_search_recs,
        "nearbysearch" : nearby_search_recs
    }

    with open("data/data_file_rec.json", "w") as write_file:
        json.dump(j_recs, write_file)

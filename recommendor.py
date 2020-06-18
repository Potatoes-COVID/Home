# Recommendor package:
# Takes in a user's search and ranks each location by their busyness
# & COVID-19 precautions. Produces an additional search for stores of
# the same type, tiered in the same manner, for more shopping options
import json
import urllib.request as url_req
import time
import googlemaps

usr = []        # user search results
nsr = []        # nearby search results
rec = []        # recommendations
loc = ""        # user (estimated) location
type = ""       # users search type
orig_name = ""
gmaps = googlemaps.Client(key='AIzaSyBMZ6xYlzyjMEZTWiXWF7F6KlvOI-rvWm0')

def Recommendor(search):
    s = json.loads(search)
    usr = s["results"]
    orig_name = usr[0]["name"]
    type = usr[0]["types"][0]
    loc = get_location(usr[0])
    get_place_info(usr, true)

    search_nearby()
    get_place_info(nsr, false)

    final_rec = sort_rec()
    rec_json = json.dumps(final_rec)
    return rec_json

def get_location(place):
    lat = usr[0]["geometry"]["location"]["lat"]
    lng = usr[0]["geometry"]["location"]["lng"]
    l = lat + ", " + lng
    return l

# restricting results to only 5 places, and if we're
# creating place objects from our nearby search, ensure
# it isn't a place of the same name
#
# places: [Google's 'Place' type]
# os: original search - boolean
def get_place_info(places, os):
    i = 0
    for p in range(places):
        if i == 5:
            return
        if !os:
            if p["name"] != orig_name:
                place = Place(p, os)
                rec += place
                i += 1
        else:
            place = Place(p, os)
            rec += place
            i += 1
    return

# sort our recommended list, separating it into two arrays
# one for the original search results, and one for the recommended
# sort each of those arrays by the rank of each place
# return an array containing those 2 arrays, which will be our
# final recommendation. The first item in each array will be
# display to the user in text above the graph
def sort_rec():
    osresults = []                                                  # original search results
    nsresults = []                                                  # nearby search results
    index = 0
    for p in range(rec):
        if p.os:
            osresults[index] = place
        else:
            nsresults[index] = place

    sorted(osresults, key=lambda place: place.rank)
    sorted(nsresults, key=lambda place: place.rank)
    return [osresults, nsresults]

# request an array of places near the user that are of the same 'Google type'
# to be used in our recommendations
def search_nearby():
    radius = 5000       # in meters, ~3.1 miles
    response = gmaps.places_nearby(key='AIzaSyBMZ6xYlzyjMEZTWiXWF7F6KlvOI-rvWm0', location=loc, radius=radius, open_now=true, type=type)
    nsr = response['results']
    return

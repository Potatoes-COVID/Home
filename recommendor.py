# Recommendor package:
# Takes in a user's search and ranks each location by their busyness
# & COVID-19 precautions. Produces an additional search for stores of
# the same type, tiered in the same manner, for more shopping options
import json
import urllib.request as url_req
import time
from config.api import APIKey

usr = []        # user search results
nsr = []        # nearby search results
rec = []        # recommendations
loc = ""        # user (estimated) location
type = ""       # users search type
orig_name = ""

def Recommendor(search):
    usr = search
    orig_name = usr[0].name
    loc = usr[0].geometry.location.toUrlValue()
    type = usr[0].types[0]
    get_place_info(usr, true)

    search_nearby()
    get_place_info(nsr, false)

    final_rec = sort_rec()
    return final_rec

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
            if place.name != orig_name:
                place = Place(p, os)
                rec += place
                i += 1
        else:
            place = Place(p, os)
            rec += place
            i += 1

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

# make a call to the Google's Places API to perform a nearby search
def request_api(url):
    response = url_req.urlopen(url)
    json_raw = response.read()
    json_data = json.loads(json_raw)
    return json_data

# request an array of places near the user that are of the same 'Google type'
# to be used in our recommendations
def search_nearby():
    apikey = APIKey
    radius = 5000       # in meters, ~3.1 miles
    api_ns_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

    loc_url = ('%s'
        '?location=%s'
        '&radius=%s'
        '&type=%s'
        '&key=%s') % (api_ns_url, loc, radius, type, apikey)

    api_response = request_api(loc_url)
    nsr = api_response['results']
    return

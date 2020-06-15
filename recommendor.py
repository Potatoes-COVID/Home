import json
import urllib.request as url_req
import time
from config.api import APIKey

usr = []        # user search results
nsr = []        # nearby search results
rec = []        # recommendations
loc = ""        # user (estimated) location
type = ""       # users search type

def Recommendor(search):
    usr = search
    loc = usr[0].geometry.location.toUrlValue()
    type = usr[0].types[0]
    get_place_info(usr, true)

    search_nearby()
    get_place_info(nsr, false)

    final_rec = sort_rec()
    return final_rec

def get_place_info(places, os):
    i = 0
    for p in range(places):
        place = Place(p, os)
        rec += place
        if i == 5:
            return
        i += 1

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

def request_api(url):
    response = url_req.urlopen(url)
    json_raw = response.read()
    json_data = json.loads(json_raw)
    return json_data

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

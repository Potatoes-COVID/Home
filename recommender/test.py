import database as db
import nearbysearch as ns

print('test #1: database -- COMPLETE')
# plus_code = '5CCP+J8 Woodland Hills, Los Angeles, CA'
# db.Database(plus_code)

print('test #2: nearbysearch, place  & database -- IN PROGRESS')

os = False
type = 'supermarket'
# location = '34.1720465,-118.5670421'     # in-n-out in woodland hills
location = '34.2410079,-118.5401147'       # CSUN area
# db.Database(location)
ns.NearbySearch(location, type, os)

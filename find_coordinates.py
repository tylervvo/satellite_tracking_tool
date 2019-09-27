#this script is not used, however it is pretty nifty:
#given a city, returns the coordinates to use for satellite tracking

import googlemaps
import sys

api_key = 'AIzaSyAX6BHi47AuAlkCUEVEaUC4vBSUr0TBM2I'

gm = googlemaps.Client(key=api_key)
if len(sys.argv) > 1:
	search_value = " "
	search_value = search_value.join(sys.argv[1:])
	geocode_result = gm.geocode(sys.argv[1])[0]
	viewport = geocode_result['geometry']['viewport']
	southwest = viewport['southwest']
	northeast = viewport['northeast']
	print("COORDINATES OF {}: Southwest Coordinate: {}, Northeast Coodinate: {}".format(search_value, southwest, northeast))
else:
	print("Provide a city to find the coordinates")


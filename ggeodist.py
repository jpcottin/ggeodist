from flask import Flask,request
import csv
from math import radians, cos, sin, asin, sqrt

def zipDictCreate(geofile):
    """ Put the zipcode in a dict with the tuple (Lat, Long) ."""
    d=dict()
    with open(geofile, 'rb') as geocsvfile:
                    fieldnames = ['ZipCode', 'Lat', 'Long']
                    georeader = csv.DictReader(geocsvfile, fieldnames=fieldnames)
                    for ziprow in georeader:
                        d[ziprow['ZipCode']]=(ziprow['Lat'],ziprow['Long']) 
    return (d)


app = Flask(__name__)

@app.route("/ggeodist/<string:lat1>/<string:lon1>/<string:lat2>/<string:lon2>/")

def calculate(lat1,lon1,lat2,lon2):
	try:
		lat1, lon1, lat2, lon2  = float(lat1), float(lon1), float (lat2), float (lon2)
	except ValueError:
		abort(404)

	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula  ( in KM) 
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	# Radius of earth in kilometers is 6371
	km = 6371 * c
	return '' + str(km)

@app.route("/geodist/<string:lat1>/<string:lon1>/<string:lat2>/<string:lon2>/")

def calculate_print(lat1,lon1,lat2,lon2):
	try:
		lat1, lon1, lat2, lon2  = float(lat1), float(lon1), float (lat2), float (lon2)
	except ValueError:
		abort(404)

	result = 'Distance between (' + str(lat1)+ ',' + str(lon1) + ') and ('+ str(lat2)+ ',' + str(lon2) + ') is '
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula  ( in KM) 
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	# Radius of earth in kilometers is 6371
	km = 6371 * c
	result =  result + str(km)
	return result

@app.route("/geodistz/<string:zip1>/<string:zip2>/")

def zipCodeDistancePrint(zip1,zip2):
	dictZipcode=zipDictCreate('zipcode_geo.csv')
	if not str(zip1) in dictZipcode:
		return "ZipCode " + zip1 + " not found"
	if not str(zip2) in dictZipcode:
		return "ZipCode " + zip2 + " not found"
	try:
		lat1, lon1, lat2, lon2  = float(dictZipcode[str(zip1)][0]), float(dictZipcode[str(zip1)][1]), float (dictZipcode[str(zip2)][0]), float (dictZipcode[str(zip2)][1])
	except ValueError:
		abort(404)

	result = 'Distance between '+zip1+ ' (' + str(lat1)+ ',' + str(lon1) + ') and '+zip2+ ' ('+ str(lat2)+ ',' + str(lon2) + ') is '
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula  ( in KM) 
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	# Radius of earth in kilometers is 6371
	km = 6371 * c
	result =  result + str(km) + " Km"
	return result

if __name__ == "__main__":
	global dictZipcode
	dictZipcode=zipDictCreate('zipcode_geo.csv')
	app.run(debug=True)


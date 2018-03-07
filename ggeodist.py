from flask import Flask,request
from math import radians, cos, sin, asin, sqrt

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


if __name__ == "__main__":
    app.run(debug=True)




from flask import Flask, request, abort
import csv
from math import radians, cos, sin, asin, sqrt

def zipDictCreate(geofile):
    d = dict()
    with open(geofile, 'r') as geocsvfile:
        fieldnames = ['ZipCode', 'Lat', 'Long']
        georeader = csv.DictReader(geocsvfile, fieldnames=fieldnames)
        for ziprow in georeader:
            d[ziprow['ZipCode']] = (ziprow['Lat'], ziprow['Long'])
    return d


def haversine(lat1, lon1, lat2, lon2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    return 6371 * 2 * asin(sqrt(a))


app = Flask(__name__)
dictZipcode = zipDictCreate('zipcode_geo.csv')


@app.route("/ggeodist/<string:lat1>/<string:lon1>/<string:lat2>/<string:lon2>/")
def calculate(lat1, lon1, lat2, lon2):
    try:
        lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)
    except ValueError:
        abort(404)
    return str(haversine(lat1, lon1, lat2, lon2))


@app.route("/geodist/<string:lat1>/<string:lon1>/<string:lat2>/<string:lon2>/")
def calculate_print(lat1, lon1, lat2, lon2):
    try:
        lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)
    except ValueError:
        abort(404)
    km = haversine(lat1, lon1, lat2, lon2)
    return f'Distance between ({lat1},{lon1}) and ({lat2},{lon2}) is {km}'


@app.route("/geodistz/<string:zip1>/<string:zip2>/")
def zipCodeDistancePrint(zip1, zip2):
    if zip1 not in dictZipcode:
        return f"ZipCode {zip1} not found"
    if zip2 not in dictZipcode:
        return f"ZipCode {zip2} not found"
    try:
        lat1 = float(dictZipcode[zip1][0])
        lon1 = float(dictZipcode[zip1][1])
        lat2 = float(dictZipcode[zip2][0])
        lon2 = float(dictZipcode[zip2][1])
    except ValueError:
        abort(404)
    km = haversine(lat1, lon1, lat2, lon2)
    return f'Distance between {zip1} ({lat1},{lon1}) and {zip2} ({lat2},{lon2}) is {km} Km'


if __name__ == "__main__":
    app.run(debug=True)

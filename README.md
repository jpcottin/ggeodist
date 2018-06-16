# ggeodist
Geodist calculations

This is the GitHub repo deployed via heroku on https://ggeodist.herokuapp.com/ggeodist/10/-50/-0.8/-18.70/

The ggeodist has this format 
@app.route("/ggeodist/<string:lat1>/<string:lon1>/<string:lat2>/<string:lon2>/")

It calculates the distance ( in kilometers ) of the 2 points ( (lat1, long1), (lat2, long2) )

Example 
`https://ggeodist.herokuapp.com/ggeodist/10/-50/-0.8/-18.70/`  -> 3665.914984157973

Other example (distance between San Francisco and San Jose) 

`curl https://ggeodist.herokuapp.com/ggeodist/37.7749295/-122.4194155/37.3382082/-121.8863286/`

67.57488345435594

--
Addition of calculation between 2 US Zipcodes

`curl https://ggeodist.herokuapp.com/geodistz/94105/58008/`
This would return:
`Distance between 94105 (37.789864,-122.393665) and 58008 (46.309281,-97.000547) is 2287.6016255001755 Km`





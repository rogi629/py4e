#Goal:  Calling a JSON API - See assignment_3.txt -

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

#This code is intended to automatically use the py4e API endpoint if no API key for google is available.
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Loops input for User until they manually break by pressing enter
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

#this code auto creates the correct syntax for api lookup from a created dictionary with 'address' and 'key' keys
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

#opens code and decodes the data into readable format
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

#tries the JSON operation to create a dictionary/list
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))
    
#finds the place_id amongst the dictionary
    place = js['results'][0]['place_id']
    print(place)
    #location = js['results'][0]['formatted_address']
    #print(location)

#!/usr/bin/python
import requests
import json
print 'ENTER POSTCODE IN UPPERCASE WITH NO SPACES eg DD11AA'
postcode = raw_input('Please enter your postcode: ')

#declare the api url and get a response
url = "http://api.postcodes.io/postcodes/{0}".format(postcode)
response = requests.get(url)

#convert it to a dict, and strip the results to a new dict
json_data = json.loads(response.text)
result_dict = json_data['result']
#print result_dict # uncomment this to see the full json

# pass specific values to varilables and print results
for key, value in result_dict.items():
    if "nhs_ha" == key:
	print value
	print "is your NHS local Health Authority"
    if "longitude" == key:
	print value
	print "is the longitude of your address"
    if "latitude" == key:
	print value
	print "is the latitude of your address"
    if "parliamentary_constituency" == key:
	print value
	print "Is your parlimentary constituency"
	

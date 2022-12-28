#Goal: Extracting Data from JSON - see assignment_2.txt -

#importing url lib, json, and ssl certificate
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
print('Retrieving:', url)
#Opens url into a readable JSON file
data = urllib.request.urlopen(url, context=ctx).read().decode()
#print(data)

#creating a dictionary out of the JSON data aquired from the web
js = json.loads(data)
#print(js)
#taking list and finding relevant dictionary
info = js['comments']
print(info)
##print('User count:', len(info))

sum = 0
#parses through dictionary for each critical item within list.
for item in info:
    value = item['count']
    #alternate code
    #value = info[x]['count'] with an x = 0 and x += 1 expression, does essentially same thing but more complicated
    #print(value)
    sum += value
print(sum)

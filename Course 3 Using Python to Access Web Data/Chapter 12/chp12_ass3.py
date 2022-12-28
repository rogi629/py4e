#Goal: Following Links in Python - See assignment_3.txt in folder -

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Request Url, Counts, pos from user
url = input('Enter - ')
counts = int(input('Enter count: '))
pos = int(input('Enter position: '))

count = 0
#Run program Once initially, then repeat process X number of times
while count <= counts:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print('Retrieving: ', url)
    tags = soup('a')
#Append links retrieved from anchor tags and find the Yth position url to repeat this process in X number of times
    links = list()
    for tag in tags:
        links.append(tag.get('href', None))
        #print(tag.get('href', None))
        #print(links)
    url = links[pos-1]
    count += 1

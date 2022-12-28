#Goal: Extracting Data from XML - See assignment_1.txt in folder - 

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
print('Retrieving:', url)
#Opens url into a readable file
xml = urllib.request.urlopen(url, context=ctx).read()
#print(xml.decode())

#converts string file of xml to a list of elements in an xml tree
tree = ET.fromstring(xml)
#makes a list of xml trees for each comments/comment element
lst = tree.findall('comments/comment')
#print('User count:', len(lst))

sum = 0
count = 0
#pulls <count> element from tree, and spits out the text value associated as int to be summed.
for item in lst:
    #print('Name:', item.find('name').text)
    #print('Count:', item.find('count').text)
    count += 1
    sum += int(item.find('count').text)
print('Count:', count)
print('Sum of #s', sum)

#Alternate method
#counts = tree.findall('.//count') --- This is the same as above code. Pulls down to count within xml tree. Not sure what './/' syntax is
#for count in counts:
#    sum += int(count.text)

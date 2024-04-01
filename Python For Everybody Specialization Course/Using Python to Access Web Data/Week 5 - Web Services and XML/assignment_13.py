import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter url: ')
xml = urllib.request.urlopen(url).read()
print('Retrieving', url)
print('Retrieved', len(xml), 'characters')

root = ET.fromstring(xml)

lst = root.findall('.//count')
print('Count:', len(lst))

total = 0
for item in lst:
    total = total + int(item.text) 
print('Sum:', total)
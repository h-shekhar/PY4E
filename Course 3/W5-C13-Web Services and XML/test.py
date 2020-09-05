'''
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the
comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and
the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_938380.xml (Sum ends with 42)
'''


import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter url: ')
xml = urllib.request.urlopen(url).read()
print('Retrieving', url)
print('Retrieved', len(xml), 'characters')

#parses XML from a string directly into the root Element of the parsed tree.
root = ET.fromstring(xml)

#use an XPath selector string look through the entire tree of XML for any tag named 'count'
lst = root.findall('.//count')
print('Count:', len(lst))

total = 0
for item in lst:
    total = total + int(item.text)
print('Sum:', total)

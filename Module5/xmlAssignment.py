import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

testurl = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_74338.xml'
uh = urllib.request.urlopen(url)

total = 0
count = 0

data = uh.read()
print('Retrieved', len(data), 'characters')
print('Retrieved', url)
tree = ET.fromstring(data)
data.decode()
results = tree.findall('comments/comment')
for values in results:
    count += 1
    data = values.find('count')
    # print(data.text)
    total = total + int(data.text)

print(count)
print(total)

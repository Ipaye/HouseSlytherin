# http://py4e-data.dr-chuck.net/comments_42.json
import urllib.request, urllib.parse
import json

total = 0
count = 0
url = input('::::::::Enter a Url - ')
print('Retrieving data from - ', url)

req = urllib.request.urlopen(url)
requestData = req.read()

data = json.loads(requestData)

for value in data['comments']:
    count += 1
    total = total + int(value['count'])

print(count)
print('Sum is: ', total)

# http://py4e-data.dr-chuck.net/known_by_Fikret.html

import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

# Session handling
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

linkArr = []

# All inputs
url = input('Enter - ')
position = int(input('Enter Position - '))
position = position - 1
count = int(input('Enter Count - '))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags

while count >= 1:
    # Retrieve all of the anchor tags
    links = soup('a')
    print(links[position].get('href', None))
    url = links[position].get('href', None)

    # Add names to array
    linkArr.append(links[position].contents[0])

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    count = count - 1

print(linkArr)
print(linkArr[len(linkArr)-1])




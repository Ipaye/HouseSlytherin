# http://py4e-data.dr-chuck.net/known_by_Fikret.html

import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
arr = []
linkArr = []

def getAllLinks(value):
    i = 0
    while i < 4:
        html = urllib.request.urlopen(value, context=ctx).read()
        handle = BeautifulSoup(html, 'html.parser')

        # Retrieve all of the anchor tags
        aLinks = handle('a')
        for lnk in aLinks:
            print(lnk)
            countLink = 1
            if countLink == 3:
                print(lnk.get('href', None))
                linkArr.append(lnk.get('href', None))
                arr.append(lnk.contents[0])
            countLink += 1

        i += 1

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
getAllLinks(url)
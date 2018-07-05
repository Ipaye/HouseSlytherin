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
count = 1
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
links = soup('a')
for link in links:
if count == 18:
    linkArr.append(link.get('href', None))
    arr.append(link.contents[0])
count += 1
print(arr)
print(linkArr)

# def GetAllLinks(value):
#     countLink = 0
#     htmlDoc = urllib.request.urlopen(value, context=ctx).read()
#     handle = BeautifulSoup(htmlDoc, 'html.parser')
#
#     # Retrieve all of the anchor tags
#     aLinks = handle('a')
#     for lnk in aLinks:
#         if countLink == 3:
#             linkArr.append(lnk.get('href', None))
#             arr.append(lnk.contents[0])
#         countLink += 1
#


# while (1 < 3):
#     length = linkArr[len(linkArr) - 1]
#     GetAllLinks(length)
#
# print(linkArr);
# print(arr)

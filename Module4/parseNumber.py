# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count = 0
total = 0

# Retrieve all of the anchor tags
spans = soup('span')
for span in spans:
    count += 1
    # Look at the parts of a span
    # print('span:', span)
    # print('Contents:', span.contents[0])
    values = int(span.contents[0])
    total += values
    # print('Attrs:', span.attrs)

print('Count', count)
print('Sum', total)
# http://py4e-data.dr-chuck.net/comments_42.html

import urllib.request
import urllib.parse
import urllib.error

# Code to read a file from a Url and count the Number of words in the file
# First method
"""
 fileHandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fileHandle:
    print(line.decode().strip())
 """

# Second Method
"""
 fileHandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()

for line in fileHandle:
    wordInLine = line.decode().split()

    for word in wordInLine:
        count[word] = count.get(word, 0) + 1

print(count)
"""


# Method 3: Abstracting into a function

def countWordsInWedpage(url):
    wordCount = dict()
    fileGotten = urllib.request.urlopen(url)
    for Lines in fileGotten:
        wordInALine = Lines.decode().split()
        for aWord in wordInALine:
            wordCount[aWord] = wordCount.get(aWord, 0) + 1
    print(wordCount)


print(countWordsInWedpage('http://ipaye.me'))

# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#  You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09: 14: 16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
hoursGotten = list()
count = dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

for emailLines in handle:
    if not emailLines.startswith("From "):
        continue
    hoursTrimmed = emailLines.strip().split(' ')[6]
    hoursDetails = hoursTrimmed.split(':')[0]
    hoursGotten.append(hoursDetails)
    # print(hoursDetails)
for time in hoursGotten:
    count[time] = count.get(time, 0) + 1

tempArr = list()
for key, value in count.items():
    newTp = (key, value)
    tempArr.append(newTp)

tempArr = sorted(tempArr, reverse=False)
# print(tempArr)

for k, v in tempArr:
    print(k, v)

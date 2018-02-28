fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.strip()
    lineTemp = line.split(" ")
    for words in lineTemp:
        words.rstrip()
        if words not in lst:
            lst.append(words.strip())

lst.sort()
print(lst)

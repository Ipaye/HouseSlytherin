# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail
#  messages.
#  The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the
#  most prolific committer.

emailGotten = list()
count = dict()
largest = -1
emailTBF = None

fhand = input('Enter in the file Name: ')
# if len(fhand) < 1:
try:
    emailFile = open(fhand)
except:
    print('File cannot be opened:', fhand)
    exit()

for emailLines in emailFile:
    if not emailLines.startswith("From: "):
        continue
    emailTrimmed = emailLines.strip().split(' ')[1]
    emailGotten.append(emailTrimmed)

# print(emailGotten)
for email in emailGotten:
    count[email] = count.get(email, 0) + 1
for key, value in count.items():
    if value > largest:
        largest = value
        emailTBF = email


print(largest, emailTBF)

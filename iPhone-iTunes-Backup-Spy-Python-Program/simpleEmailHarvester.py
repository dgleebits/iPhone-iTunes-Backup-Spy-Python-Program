#! /usr/bin/python
'''
This program will snarf email addresses from Online Staff Directory
'''

import urllib2

mylist = []
emailAddressList = []
data = []
my_target = 'http://ccapps.example.ca/phonebook/phonebook.serv?search=a'

file_handler = urllib2.urlopen(my_target)
data = file_handler.readlines()

for line in data:
    if 'mailto:' in line:
  	emailAddressString = line
		emailAddress = emailAddressString[emailAddressString.find('mailto:')+7:emailAddressString.find('@example.ca')+10]
		emailAddressList.append(emailAddress)
		mylist = emailAddressList[:]
        
if mylist:
    mylist.sort()
    last = mylist[-1]
    for i in range(len(mylist)-2, -1, -1):
        if last == mylist[i]:
            del mylist[i]
        else:
            last = mylist[i]

print mylist	
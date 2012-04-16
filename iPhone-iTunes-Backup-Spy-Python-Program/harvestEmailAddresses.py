#!/usr/bin/python
'''This program enumerates the website based phonebook and harvests email addresses'''

import urllib2
targetURL = "http://somewebaddress"
alphabet = "abcdefghijklmnopqrstuvwxyz"
beginTAG = "mailto:"
beginTAGvalue = len(beginTAG)
endTAG = "@someDomain.whatever"
endTAGvalue = len(endTAG)
  
def main():
	#looping thru alphabet - GET request for each letter
	for letter in alphabet:
		print "Here are the email addresses for %s" %letter
		print "*"*100
		f = urllib2.urlopen(targetURL+letter)
		line = f.readline()
		for line in f:
			extractEmail(line)

def extractEmail(line):
    ''' Uses slice on line to get email address '''
    lSS = line[(line.find(beginTAG)+beginTAGvalue):(line.find(endTAG)+endTAGvalue)]
    if len(lSS) > endTAGvalue:
		print lSS
    
if __name__ == "__main__":
    main()
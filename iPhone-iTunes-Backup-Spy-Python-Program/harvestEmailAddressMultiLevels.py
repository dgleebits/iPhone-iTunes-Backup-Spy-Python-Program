#!/usr/bin/python
''' This webscraper hits http://app.example.com/qf_net/Default.aspx and http://app.example.com/QFOrgChart_net/default.aspx?id=1056 
and http://app.example.com/QFOrgChart_net/orgchart.html and parses http://app.example.com/Qf_Net/DirectoryDetail.aspx?ID=14753&name=Sheila 
from webpage.  Email address harvester. '''

def main():
  ''' This main function loops thru GET's '''
	IDLimit = 20
	myCounter = 14
	myCounter2 = 0
	myList = {}
	defaultTargetURL = 'http://app.example.com/QFOrgChart_net/default.aspx?id='
	search_value = 'default.aspx?id='
	searchTerm = 'DirectoryDetail.aspx?ID='
	splitItem = '"'
	beginTAG = 'mailto:'
	beginTAGvalue = len(beginTAG)
	endTAG = '@example.com'
	endTAGvalue = len(endTAG)

	while myCounter<IDLimit:
		f = urllib2.urlopen(defaultTargetURL+str(myCounter))
		print defaultTargetURL+str(myCounter)
		webPage = f.read()
		myCounter=myCounter+1
		if parse(webPage) == None:
			pass
		else:
			entryOnPage = webPage.count(searchTerm)
			if entryOnPage > 0:
				stuff = webPage.split(splitItem)
				while myCounter2 < entryOnPage:
					for myLink in stuff:
						if searchTerm in myLink:
							myList[myCounter2] = myLink
							myCounter2 = myCounter2+1
				for k, v in myList.iteritems():
					valueLink = "http://app.example.com"+v
					try:
						f2 = urllib2.urlopen(valueLink)
						webPageSecondLevel = f2.read()
						extractEmail(webPageSecondLevel)
					except urllib2.HTTPError, error:
						contents = error.read()
#are these on an endless loop?

def parse(myList):                                                                
    ''' Function splits webpage into list and parses email addresses '''
    splitItem = '"'
    searchTerm = 'DirectoryDetail.aspx?ID='
    search_value = 'default.aspx?id='
    beginTAG = 'mailto:'
    beginTAGvalue = len(beginTAG)
    endTAG = '@example.com'
    endTAGvalue = len(endTAG)
    stuff = myList.split(splitItem)
    for myLink in stuff:
    	if searchTerm in myLink:
    		return myLink
    		
def extractEmail(line):
   ''' Uses slice on line to get email address '''
   splitItem = '"'
   searchTerm = 'DirectoryDetail.aspx?ID='
   search_value = 'default.aspx?id='
   beginTAG = 'mailto:'
   beginTAGvalue = len(beginTAG)
   endTAG = '@example.com'
   endTAGvalue = len(endTAG)
   lSS = line[(line.find(beginTAG)+beginTAGvalue):(line.find(endTAG)+endTAGvalue)]
   if len(lSS) > endTAGvalue:
		print lSS
            
if __name__ == "__main__":
	import urllib2
	main()
        	
            
        

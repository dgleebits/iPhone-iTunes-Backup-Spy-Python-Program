#! /usr/bin/python
'''This program will snarf email addresses from Online Staff Directory'''

import urllib2

my_dict = {}
my_emailAddresses = {}
data = []
my_counter = 0
my_target = 'http://m.directory.xxx/index.cfm/person/search#'
search_string = '<a href="/index.cfm/person/get?person_id='
beginTAG = '<a href="/index.cfm/person/get?person_id='
endTAG = '" data-ajax="false"'
beginTAGvalue = len(beginTAG)
endTAGvalue = len(endTAG)

def main():
    '''main function to open URL and call emailAddress function'''
    file_handler = urllib2.urlopen(my_target)
    data = file_handler.readlines()
    eNumData (data, my_counter,my_dict)
    print my_dict
    extractEmail(my_dict)

def eNumData(data, my_counter, my_dict):
    '''function to create dict of emailAddresses found on webpages'''
    for k,v in enumerate(data):
         if search_string in v:
             my_counter = my_counter + 1       
             my_dict[k] = v
    return my_dict

def extractEmail(my_dict):
   ''' Uses slice on line to get email address'''
   for k,v in my_dict.iteritems():
         if beginTAG in v:   #iterating thru list looking for tag
             unstripped = v  #this assignment makes it a string from list item
             emailAddress = unstripped[(unstripped.find(beginTAG)+beginTAGvalue):(unstripped.find(endTAG)+endTAGvalue)]
             if len(emailAddress) > endTAGvalue:
          print emailAddress

if __name__ == "__main__":
    main()

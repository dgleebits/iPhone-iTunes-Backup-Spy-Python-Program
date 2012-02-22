#!/usr/bin/env python
# encoding: utf-8

import sqlite3
import time
import sys
import os
import codecs 

"""
iphone_sms_spy.py

Decodes iphone sms database, hidden in itunes backup data files, into human readable form

*** Use program with COPY of the original data***
*** Use at own risk ***
*** Be good ***

Created by: Dan G
Create Date: Friday 5th August 2011
Contact: dangleebits@hotmail.ca
Version: 0.1 

Windows XP:  C:\Documents and Settings\(username)\Application Data\Apple Computer\MobileSync\Backup\
Windows Vista: C:\Users\(username)\AppData\Roaming\Apple Computer\MobileSync\Backup\
Mac OS X: /Users/(username)/Library/Application Support/MobileSync/Backup/

Thanks to iphone backup decoder and arrdino and viaforensics and andy for their work
"""

DEBUG = True #Set True for copy of output to file
output = """%s - %s - %s
        %s         

"""

def usage():
  print "iPhone SMS Spy Decoder\n"
  print "Usage: " + sys.argv[0] + " (Path to 3d0d7e5fb2ce288813306e4d4636395e047a3d28 file to SMS SPY) \n"
  print "Coded by Dan G"
  print "Version 0.1"

#conversion of the epoch to human
def convertDate(epoch):
  return time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime(epoch))

def main(dbfile, outputfile):

  #variables
  count = 0
  firstDate = ""
  lastDate = ""
  outFile = codecs.open(outputfile, encoding='utf-8', mode='w')

  #opening db and SQL query for SMS
  connection = sqlite3.connect(r"c:\Documents and Settings\(username)\Desktop\sms.db")
  cursor = connection.cursor()
  cursor.execute ("select flags, address, date, text from message")

  #iterating
  for row in cursor:
    flags = ""
    flags = row[0]
    if flags == 2: direction = "Received"
    if flags == 3: direction = "Sent"
    if flags == 0: direction = ""
    address = str(row[1])
    date = convertDate(row[2])
    text = unicode(row[3])

    #printing each SMS message to stdout
    outData = output % (address, direction, date, text)
    print outData

    #for output file
    if DEBUG:
      print outData
    outFile.write(outData)

    #put first Date and last Date in variables
    if count == 0:
      firstDate = date
    lastDate = date
    count += 1

  #prints the date of the first SMS and the lastest date on the last SMS
  outData = "Date Range: %s - %s" % (firstDate, lastDate)
  #toggle for file output
  if DEBUG:
    print outData
  #creation of the file output
  outFile.write(outData)
  #good citizen
  outFile.close()

if __name__ == "__main__":
  dbfile = "c:\Documents and Settings\(username)\Desktop\sms.db"
  outFile = "SMS_Spy.txt"
  main(dbfile, outFile)
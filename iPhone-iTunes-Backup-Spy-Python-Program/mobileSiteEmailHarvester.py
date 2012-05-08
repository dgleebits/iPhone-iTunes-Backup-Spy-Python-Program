import mechanize

alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Fill it out an 'a'
for letter in alphabet:
  b = mechanize.Browser()
	# Disable loading robots.txt
	b.set_handle_robots(False)
	b.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 5.0; Windows 98;)')]
	# Navigate
	b.open('http://m.directory.example.ca/index.cfm/person/searchform')
	# Choose a form
	b.select_form(nr=0)
	b['search'] = letter
	# Submit put into fh file handler contstant
	fh = b.submit()
	# read instance of fh into data constant
	data = fh.readlines()
	for line in data: 
    	if '_id=' in line:
			dataList.append(line[line.find('''_id=''')+4:line.find('''" data-ajax="false"''')])
for item in range(len(mylist)):
	response = mechanize.urlopen('http://m.directory.ubc.ca/index.cfm/person/get?person_id=' + (mylist[item]))
	dump = response.readlines()
	for line in dump:
	if 'mailto:' in line:
		print line
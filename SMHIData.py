import json, requests, pprint


#def getRain(timeString):
#	url = 'http://opendata-download-metfcst.smhi.se/api/category/pmp1.5g/version/1/geopoint/lat/58.41/lon/15.63/data.json'
#	resp = requests.get(url=url)
#	data = json.loads(resp.text)
#	dataResult =data['timeseries']
#	string = str('2015-09-05T'+timeString+'Z')
#	pp = pprint.PrettyPrinter(indent=4)
#	for fields in dataResult:
#		if(fields['validTime']==string):
#			pp.pprint("Det kommer att regna "+str(fields['pit'])+ " mm/h vid klockan "+str(timeString))

#def getTempature(timeString):
#	url = 'http://opendata-download-metfcst.smhi.se/api/category/pmp1.5g/version/1/geopoint/lat/58.41/lon/15.63/data.json'
#	resp = requests.get(url=url)
#	data = json.loads(resp.text)
#	dataResult =data['timeseries']
#	string = str('2015-09-05T'+timeString+'Z')
#	pp = pprint.PrettyPrinter(indent=4)
#	for fields in dataResult:
#		if(fields['validTime']==string):
#			return fields['t']


def getSMHIdata(timeString):
	url = 'http://opendata-download-metfcst.smhi.se/api/category/pmp1.5g/version/1/geopoint/lat/58.41/lon/15.63/data.json'
	resp = requests.get(url=url)
	data = json.loads(resp.text)
	dataResult =data['timeseries']
	string = str('2015-09-05T'+timeString+'Z')
	pp = pprint.PrettyPrinter(indent=4)
	for fields in dataResult:
		if(fields['validTime']==string):
			return fields



string = '17:00:00'
#readDataRain(string)
#readDataTempature(string)
print(getSMHIdata(string))
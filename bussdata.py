import json, requests, pprint
key = 'SOhPfNfIpquJ0DLYb33ODX44NMf6shrl'
pp = pprint.PrettyPrinter(indent=4)
urltravel = 'https://api.trafiklab.se/samtrafiken/resrobot/Search.json?apiVersion=2.1&fromId=7453854&toId=7421842&key=SOhPfNfIpquJ0DLYb33ODX44NMf6shrl&arrival=false&time=08:00&date=2015-09-07'
urltoposition = 'https://api.trafiklab.se/samtrafiken/resrobot/FindLocation.json?apiVersion=2.1&from=linkoping&coordSys=RT90&key=SOhPfNfIpquJ0DLYb33ODX44NMf6shrl'
urlfromposition = 'https://api.trafiklab.se/samtrafiken/resrobot/FindLocation.json?apiVersion=2.1&from=Ryd&centrum&coordSys=RT90&key=SOhPfNfIpquJ0DLYb33ODX44NMf6shrl'

def getlocationid(data, stringlocation):

	#if(data['from']['location']['displayname']==''Linköping ''Trädgårdstorget')

	pp = pprint.PrettyPrinter(indent=4)
	for fields in data['findlocationresult']['from']['location']:
		if(fields['displayname']==str(stringlocation)):
			print(fields['displayname'])
			return fields['locationid']
	return 0


def getbustravel(fromloc, toloc):
	#url = 'http://parkering.linkoping.se/Parkeringsdata/ParkeringsdataV1.svc/GetParkeringsytaList/66fc20e245084815af770af82d2ceef6/080000'
	#url = 'http://parkering.linkoping.se/Parkeringsdata/ParkeringsdataV1.svc/GetParkeringsytaById/66fc20e245084815af770af82d2ceef6/29_1'
	respfrom = requests.get(url=urlfromposition)
	data = json.loads(respfrom.text)
	fromlocation = getlocationid(data, fromloc)
	respto = requests.get(url=urltoposition)
	data = json.loads(respto.text)
	tolocation = getlocationid(data, toloc)
	resp = requests.get(url=urltravel)
	data = json.loads(resp.text)
	return data

	#dataResult =data['ParkingAreaNewList']
	#returnData = []
	#for fields in dataResult:
		

		#if(fields['Latitude']<58.4119 and fields['Latitude']>58.4087 and fields['Longitude']<15.6249 and fields['Longitude']>15.6089):
			#returnData.append(fields)
	#return returnData
	
# '7421842', 'Linköping Trädgårdstorget'
# '7453854', 'Ryd centrum (Linköping kn)'
getbustravel('Ryd centrum (Linköping kn)','Linköping Trädgårdstorget')
#pp.pprint(getbustravel())
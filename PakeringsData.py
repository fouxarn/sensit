import json, requests, pprint
key = '66fc20e245084815af770af82d2ceef6'
pp = pprint.PrettyPrinter(indent=4)


def getPakeringLkpgdata(timeString):
	url = 'http://parkering.linkoping.se/Parkeringsdata/ParkeringsdataV1.svc/GetParkeringsytaList/66fc20e245084815af770af82d2ceef6/080000'
	#url = 'http://parkering.linkoping.se/Parkeringsdata/ParkeringsdataV1.svc/GetParkeringsytaById/66fc20e245084815af770af82d2ceef6/29_1'
	resp = requests.get(url=url)
	data = json.loads(resp.text)
	pp = pprint.PrettyPrinter(indent=4)
	#pp.pprint(data)
	dataResult =data['ParkingAreaNewList']
	returnData = []
	for fields in dataResult:
		

		if(fields['Latitude']<58.4119 and fields['Latitude']>58.4087 and fields['Longitude']<15.6249 and fields['Longitude']>15.6089):
			returnData.append(fields)
	return returnData
	


pp.pprint(getPakeringLkpgdata("timeString"))
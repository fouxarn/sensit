import json, requests, pprint
key = '66fc20e245084815af770af82d2ceef6'

def getPakeringLkpgdata(timeString):
	url = 'http://parkering.linkoping.se/Parkeringsdata/ParkeringsdataV1.svc/GetParkeringsytaList/66fc20e245084815af770af82d2ceef6/080000'
	#url = 'http://parkering.linkoping.se/Parkeringsdata/ParkeringsdataV1.svc/GetParkeringsytaById/66fc20e245084815af770af82d2ceef6/29_1'
	resp = requests.get(url=url)
	data = json.loads(resp.text)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(data)


getPakeringLkpgdata("timeString")
import json
from urllib.request import urlopen
with urlopen("https://api.covid19india.org/data.json") as response:
    source=response.read()
# print(source)

data=json.loads(source)
# print(json.dumps(data, indent=2))
# print(len(data['raw_data']))
filename="Tests.csv"
f=open(filename,"w")
headers="Updated Time Stamp,Individuals Tested per Confirmed Cases,Positive Cases from Samples Reported,Samples Reported Today,Test Positivity Rate,Test Conducted By Private Labs, Tests per Confirmed Case,Tests per Million, Total Sample Tested\n"
f.write(headers)

for item in data['tested']:
    updatetimestamp=item['updatetimestamp']
    itc=item['individualstestedperconfirmedcase']
    pcsr=item['positivecasesfromsamplesreported']
    srt=item['samplereportedtoday']
    tpr=item['testpositivityrate']
    tcp=item['testsconductedbyprivatelabs']
    tpcc=item['testsperconfirmedcase']
    tpm=item['testspermillion']
    tst=item['totalsamplestested']
    
    
    f.write(updatetimestamp.replace(",","")+ "," +itc.replace(",","") +","+pcsr.replace(",","")+","+srt.replace(",","")+","+tpr.replace(",","")+","+tcp.replace(",","")+","+tpcc.replace(",","")+","+tpm.replace(",","")+","+tst.replace(",","")+"\n")
    # print(patientnumber, statecode, statepatientnumber, nationality,
    # detectedcity, dateannounced, age, gender, currentstatus)
f.close()

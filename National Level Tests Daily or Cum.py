import json
from urllib.request import urlopen
with urlopen("https://api.covid19india.org/data.json") as response:
    source=response.read()
# print(source)

data=json.loads(source)
# print(json.dumps(data, indent=2))
# print(len(data['raw_data']))
filename="National Level Tests Daily or Cum.csv"
f=open(filename,"w")
headers="Date (PK),Samples Reported Today,Tests Per Million,Total Samples Tested\n"
f.write(headers)

for item in data['tested']:
    date=item['updatetimestamp'][:10]
    srt=item['samplereportedtoday']
    tpm=item['testspermillion']
    tst=item['totalsamplestested']
    f.write(date+","+srt.replace(",","") +","+ tpm.replace(",","")+","+tst.replace(",","")+"\n")
    # print(patientnumber, statecode, statepatientnumber, nationality,
    # detectedcity, dateannounced, age, gender, currentstatus)
f.close()

import json
import datetime
from urllib.request import urlopen
with urlopen("https://api.covid19india.org/data.json") as response:
    source=response.read()
# print(source)
currentDT = datetime.datetime.now()
data=json.loads(source)
# print(json.dumps(data, indent=2))
# print(len(data['raw_data']))
filename="National Level Latest.csv"
f=open(filename,"w")
headers="Date, Country ID , Updated Time, Total Confirmed Cases, Total Deceased Cases, Total Recovered Cases\n"
f.write(headers)

for item in data['cases_time_series']:
    date=item['date']
    country_id=str(101)
    total_confirmed=item['totalconfirmed']
    total_deceased=item['totaldeceased']
    total_recovered=item['totalrecovered']
    f.write(date +","+ country_id + ","+ str(currentDT) + "," +total_confirmed.replace(",","") +","+ total_deceased.replace(",","")+","+ total_recovered.replace(",","")+"\n")
    # print(patientnumber, statecode, statepatientnumber, nationality,
    # detectedcity, dateannounced, age, gender, currentstatus)
f.close()

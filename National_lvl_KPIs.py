import json
from urllib.request import urlopen
with urlopen("https://api.covid19india.org/data.json") as response:
    source=response.read()
# print(source)

data=json.loads(source)
# print(json.dumps(data, indent=2))
# print(len(data['raw_data']))
filename="National_lvl_KPIs.csv"
f=open(filename,"w")
headers=" State ID ,Last Updated Time,Total Confirmed Cases,Total Deceased Cases,Total Recovered Cases,Total Active Cases,Delta Confirmed Cases,Delta Deceased Cases,Delta Recovered Cases\n"
f.write(headers)

for item in data['statewise']:
    state_id=item['statecode']
    lastupdatedtime=item['lastupdatedtime']
    total_confirmed=item['confirmed']
    total_deceased=item['deaths']
    total_recovered=item['recovered']
    active=item['active']
    delta_cofirmed=item['deltaconfirmed']
    delta_deceased=item['deltadeaths']
    delta_recovered=item['deltarecovered']
    f.write(state_id.replace(",","")+","+lastupdatedtime.replace(",","") +","+ total_confirmed.replace(",","") +","+ total_deceased.replace(",","")+","+total_recovered.replace(",","")+","+ active.replace(",","") +","+ delta_cofirmed.replace(",","")+","+ delta_deceased.replace(",","")+","+delta_recovered.replace(",","")+"\n")
    break
    # print(patientnumber, statecode, statepatientnumber, nationality,
    # detectedcity, dateannounced, age, gender, currentstatus)
f.close()

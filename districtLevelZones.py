import json
from urllib.request import urlopen
with urlopen("https://api.covid19india.org/zones.json") as response:
    source=response.read()

data=json.loads(source)
filename="districtLevelZones.csv"
f=open(filename,"w")
headers = "District ID, State ID, Last Updated, Zone\n"
f.write(headers)

for item in data['zones']:
    district_id = item["districtcode"]
    state_id = item["statecode"]
    lastupdated = item["lastupdated"]
    zone = item["zone"]

    f.write(district_id.replace(",","") +","+ state_id.replace(",","") +","+ lastupdated +","+ zone.replace(",","")+"\n")
f.close()

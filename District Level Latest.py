import json
import datetime
from urllib.request import urlopen
with urlopen("https://api.covid19india.org/v2/state_district_wise.json") as response:
    source=response.read()
# print(source)
currentDT = datetime.datetime.now()
data=json.loads(source)
# print(json.dumps(data, indent=2))
# print(len(data['raw_data']))
filename="District Level Latest.csv"
f=open(filename,"w")
headers="State ID,Ditrict Name,Last Updated Time,Total Confirmed Cases,Total Deceased Cases,Total Recovered Cases,Total Active Cases,Delta Confirmed Cases,Delta Deceased Cases,Delta Recovered Cases\n"
f.write(headers)

for i in data:
    state_id=i['statecode']
    for item in i['districtData']:
        district_id=item['district']
        last_updated_time=str(currentDT)
        total_con=item['confirmed']
        total_dec=item['deceased']
        total_rec=item['recovered']
        total_act=item['active']
        
            
        delta_con=item['delta']['confirmed']
        delta_dec=item['delta']['deceased']
        
        delta_rec=item['delta']['recovered']
        f.write(str(state_id)+","+str(district_id)+","+last_updated_time +","+str(total_con) +","+str(total_dec) +","+str(total_rec)+","+str(total_act) +","+str(delta_con)+","+str(delta_dec)+","+str(delta_rec)+"\n")
            
f.close()

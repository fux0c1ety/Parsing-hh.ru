import requests
import time
import random

url= 'https://api.hh.ru/vacancies/'
result_url = 'https://hh.ru/vacancy/'

for i in range(35787520, 1, -1):
    f = open('list.csv', 'a')
    d = requests.get(url+str(i)).json()
    print()
    try:
        if (d["salary"])["from"]==None:
            f.write(str(d["name"])+'.'+str((d["salary"])["to"])+','+str((d["salary"])["currency"])+','+str(d['created_at'])+','+url+str(i)+'\n')
            print(d["name"], (d["salary"])["to"], (d["salary"])["currency"], d['created_at']+' '+url+str(i))
        elif (d["salary"])["to"]==None:
            f.write(str(d["name"])+'.'+str((d["salary"])["from"])+','+str((d["salary"])["currency"])+','+str(d['created_at'])+','+url+str(i)+'\n')
            print(d["name"], (d["salary"])["from"], (d["salary"])["currency"], d['created_at']+' '+url+str(i))
        else:
            f.write(str(d["name"])+'.'+str((d["salary"])["from"])+','+str((d["salary"])["to"])+','+str((d["salary"])["currency"])+','+str(d['created_at'])+','+url+str(i)+'\n')            
            print(d["name"], (d["salary"])["from"], '-' ,(d["salary"])["to"], (d["salary"])["currency"], d['created_at']+' '+url+str(i))
    except:
        time.sleep(random.uniform(0, 3))
    f.close()

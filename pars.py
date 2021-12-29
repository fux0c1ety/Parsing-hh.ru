import requests
import time
import random

API_URL = 'https://api.hh.ru/vacancies/'
SITE_URL = 'https://hh.ru/vacancy/'
ID = 35787520

while True:
    ID += 1
    f = open('list.csv', 'a')
    d = requests.get(API_URL+str(ID)).json()
    print()
    try:
        if (d["salary"])["from"]==None:
            f.write(str(d["name"])+';'+str((d["salary"])["to"])+';'+str((d["salary"])["currency"])+';'+str(d['created_at'])+';'+SITE_URL+str(ID)+'\n')
            print(d["name"], (d["salary"])["to"], (d["salary"])["currency"], d['created_at']+' '+SITE_URL+str(ID))
        elif (d["salary"])["to"]==None:
            f.write(str(d["name"])+';'+str((d["salary"])["from"])+';'+str((d["salary"])["currency"])+';'+str(d['created_at'])+';'+SITE_URL+str(ID)+'\n')
            print(d["name"], (d["salary"])["from"], (d["salary"])["currency"], d['created_at']+' '+SITE_URL+str(ID))
        else:
            f.write(str(d["name"])+';'+str((d["salary"])["from"])+';'+str((d["salary"])["to"])+';'+str((d["salary"])["currency"])+';'+str(d['created_at'])+';'+SITE_URL+str(ID)+'\n')  
            print(d["name"], (d["salary"])["from"], '-' ,(d["salary"])["to"], (d["salary"])["currency"], d['created_at']+' '+SITE_URL+str(ID))

    except:
        time.sleep(random.uniform(0, 0.1))
    f.close()

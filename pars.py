import requests
import time
import random

API_URL = 'https://api.hh.ru/vacancies/'
SITE_URL = 'https://hh.ru/vacancy/'
ID = 35787520

OUT_FILE = open('list.csv', 'a')

while True:
    ID += 1
    response = requests.get(API_URL+str(ID)).json()
    print()
    try:
        if (response["salary"])["from"]==None:
            resstr = response["name"]+';'+' '+';'+str((response["salary"])["to"])+';'+(response["salary"])["currency"]+';'+str(response['created_at'])+';'+SITE_URL+str(ID)+'\n'
            OUT_FILE.write(resstr)
            print(response["name"], (response["salary"])["to"], (response["salary"])["currency"], response['created_at']+' '+SITE_URL+str(ID))
        elif (response["salary"])["to"]==None:
            resstr = response["name"]+';'+str((response["salary"])["from"])+';'+' '+';'+(response["salary"])["currency"]+';'+str(response['created_at'])+';'+SITE_URL+str(ID)+'\n'
            OUT_FILE.write(resstr)
            print(response["name"], (response["salary"])["from"], (response["salary"])["currency"], response['created_at']+' '+SITE_URL+str(ID))
        else:
            resstr = response["name"]+';'+str((response["salary"])["from"])+';'+str((response["salary"])["to"])+';'+response["salary"]["currency"]+';'+response['created_at']+';'+SITE_URL+ID+'\n' 
            OUT_FILE.write(resstr)  
            print(response["name"], (response["salary"])["from"], '-' ,(response["salary"])["to"], (response["salary"])["currency"], response['created_at']+' '+SITE_URL+str(ID))

    except TypeError:
        time.sleep(random.uniform(0, 0.1))

    except KeyError:
        time.sleep(random.uniform(0, 0.1))

    except KeyboardInterrupt:
        f.close()

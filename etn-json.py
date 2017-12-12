# import json
import requests, time
a = 1
while a == 1:
    url = requests.get('https://api.nanopool.org/v1/etn/balance/etnjyz4xSSYYsTb9e4NGut8djRgJABCMxNi1AnMKNPepQu2nQPAJcZU5ifUPHoN1yEX5ZwHHYRpLk8B9V5YzCKkRA5Cvxk8YU6')
    data_json = url.json()
    etn = data_json['data']

    if etn < 64:
        etn_to_euro = float(etn) * 0.088418
        print ("Nombre d'ETN :", etn)
        print ("ETN en euro : ", etn_to_euro)
        time.sleep(10)
        continue
    else:
        print ("tu es riche")

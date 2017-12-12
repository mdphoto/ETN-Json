# -*- coding: utf-8 -*-
import requests, time

def pull_data():
    """Import Electroneum json on nanopool"""
    url = requests.get('https://api.nanopool.org/v1/etn/balance/etnjyz4xSSYYsTb9e4NGut8djRgJABCMxNi1AnMKNPepQu2nQPAJcZU5ifUPHoN1yEX5ZwHHYRpLk8B9V5YzCKkRA5Cvxk8YU6')
    data_json = url.json()
    data = data_json['data']
    return data

etn = pull_data()
while 1 == 1:
    if etn < 100:
        # """Check if the total is sup 100 and display your ETN"""
        etn_to_euro = float(etn) * 0.088418
        print ("Nombre d'ETN :", etn)
        print ("ETN en euro : ", etn_to_euro)
        time.sleep(60)
    else:
        # """Alert if the total is up to 100"""
        print ("Nanopool ETN transfer to walett was done")

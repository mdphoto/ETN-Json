# -*- coding: utf-8 -*-
import requests, time
from tkinter import *



def pull_data(a):
    url = requests.get('https://api.nanopool.org/v1/etn/balance/etnjyz4xSSYYsTb9e4NGut8djRgJABCMxNi1AnMKNPepQu2nQPAJcZU5ifUPHoN1yEX5ZwHHYRpLk8B9V5YzCKkRA5Cvxk8YU6')
    data_json = url.json()
    etn = data_json['data']




a = 1
while a == 1:
    """Import Electroneum json on nanopool"""
pull_data()
    if etn < 100:
        """Check if the solde is sup 100 and display your ETN"""
        etn_to_euro = float(etn) * 0.088418
        print ("Nombre d'ETN :", etn)
        # print ("ETN en euro : ", etn_to_euro)
        time.sleep(10)
        continue
    else:
        """Alerte if the solde is up to 100"""
        fenetre = Tk()
        label = Label(fenetre, text="Nanopool ETN transfer to walett was done")
        label.pack()
        print ("Nanopool ETN transfer to walett was done")

for etn
fenetre = Tk()
etn = Label(fenetre, text=etn)
etn.pack()
euro = Label(fenetre, text=etn_to_euro)
euro.pack()
fenetre.mainloop()

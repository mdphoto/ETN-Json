# -*- coding: utf-8 -*-
import requests, time
from tkinter import *



def pull_data():
    url = requests.get('https://api.nanopool.org/v1/etn/balance/etnjyz4xSSYYsTb9e4NGut8djRgJABCMxNi1AnMKNPepQu2nQPAJcZU5ifUPHoN1yEX5ZwHHYRpLk8B9V5YzCKkRA5Cvxk8YU6')
    data_json = url.json()
    etn = data_json['data']
    return etn


# while 1 == 1:
#     time.sleep(10)
#     pull_data()
etn = pull_data()
#     if etn < 68:
#         print (etn)

fenetre = Tk()
fenetre.after(10000,pull_data)
etn = Label(fenetre, text=etn)
etn.pack()
fenetre.mainloop()

# a = 1
# while a == 1:
#     """Import Electroneum json on nanopool"""
# pull_data()
#     if etn < 100:
#         print ("Nombre d'ETN :", etn)
#         time.sleep(10)
#         continue
#     else:
#
#         print ("Nanopool ETN transfer to walett was done")
#
# for etn
# fenetre = Tk()
# etn = Label(fenetre, text=etn)
# etn.pack()
# euro = Label(fenetre, text=etn_to_euro)
# euro.pack()
# fenetre.mainloop()

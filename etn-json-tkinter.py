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
etn =  StringVar()
#     if etn < 68:
#         print (etn)

fenetre = Tk()

etn = Label(fenetre, textvariable=etn)
etn.pack()
fenetre.after(10000, pull_data)

fenetre.mainloop()

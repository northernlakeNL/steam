#alle imports die nodig zijn
from tkinter import *
from tkinter import ttk
import json
import os
import statistics
import pandas as pd
import numpy
import requests

#Json bestand uitlezen
with open('steam.json') as Steam:
    gamelist = json.load(Steam)

for game in gamelist:
    gamenaam = game['name']
    releasedate = game['release_date']
    
    
#scherm
root = Tk()

root.title('Steam Add-on Project')
root.state('iconic')
root.geometry('720x480')

#wdigets
name = Label(root, text=f'Naam:  ')
release = Label(root, text=f'Release Date:   ')
developer = Label(root, text=f'Developer:   ')


name.grid(row=0, column=0, sticky='w')
release.grid(row=1, column=0, sticky='w')
developer.grid(row=2, column=0, sticky='w')
root.mainloop()
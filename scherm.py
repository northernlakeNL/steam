#alle imports die nodig zijn
import tkinter as tk
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
nette_gamelist = json.dumps(gamelist, indent=4)

#scherm
root = tk.Tk()

root.title('Steam Add-on Project')
root.state('iconic')
root.geometry('720x480')

#wdigets
name = tk.Label(root, text=f'Naam:  ')

name.grid(row=0, column=0)
root.mainloop()
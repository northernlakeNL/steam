import tkinter as tk
import json
import os
import statistics
import pandas as pd
import numpy
import requests
S = open('steam.json')
gamedata = json.load(S)

root = tk.Tk()

root.title('Steam Add-on Project')
root.state('iconic')
root.geometry('720x480')

game = input('Game naam:    ')
for game in gamedata:
    print(json.dumps(game))

root.mainloop()
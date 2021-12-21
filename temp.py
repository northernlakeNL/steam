#alle imports die nodig zijn
from tkinter import *
from tkinter import ttk
import json
import os
import statistics
import pandas as pd
import numpy
import requests
from urllib.request import urlopen
from time import sleep

#values
API_key = 'AF90EFF02499BB3CDDFFF28629DEA47B'
user_ID = '76561198172219198'

#json bestand uitlezen
with open('steam.json') as Steam:
    gamelist = json.load(Steam)

#game zoeken
# game_naam = input("Welke game zoek je: ")
# for game in gamelist:
#     if game["name"] == game_naam:
#         game_code = game['appid']
#         gamenaam = game['name']
#         releasedate = game['release_date']
#         prijs = game['price']
#         achievements = game['achievements']
#         developer = game['developer']
#         platforms = game['platforms']
#URL compleet


#Data halen uit de URL


#scherm
root = Tk()
root.title('Steam Add-on Project')
root.state('iconic')
root.geometry('720x480')

#widgets
label1 = Label(root,
                text='Game of which you want your data.',
                font=18)
label1.pack(pady=5)
WantedData = Entry(root)
WantedData.pack(side=BOTTOM)

def gatherdata():
    game = WantedData.get()
    try:
        for game in gamelist:
            if game["name"] == game:
                global gamenaam
                gamenaam = game['name']
                global game_code
                game_code = game['appid']
    except:
        sleep(3.0)
        exit()

button=Button(root,
                text='Search',
                command=gatherdata)
button.pack(pady=5)

if button == True:
    URL = f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={game_code}&key={API_key}&steamid={user_ID}'
    response = urlopen(URL)
    user_game_data = json.loads(response.read())
    gamedata = Label(root,
                text=user_game_data,
                font=18)
    gamedata.pack(pady=5)
    print(user_game_data)

# gamedata = Label(root, text=f'User stats:   {user_game_data}')
# gamedata.pack(side=LEFT)
root.mainloop()
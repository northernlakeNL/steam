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

#values
API_key = 'AF90EFF02499BB3CDDFFF28629DEA47B'
user_ID = '76561198172219198'

#json bestand uitlezen
with open('steam.json') as Steam:
    gamelist = json.load(Steam)

#game zoeken
game_naam = input("Welke game zoek je: ")
for game in gamelist:
    if game["name"] == game_naam:
        game_code = game['appid']
        gamenaam = game['name']
        releasedate = game['release_date']
        prijs = game['price']
        achievements = game['achievements']
        developer = game['developer']
        platforms = game['platforms']

URL = f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={game_code}&key={API_key}&steamid={user_ID}'

response = urlopen(URL)
user_game_data = json.loads(response.read())

#vriendenlijst
# friendlist = requests.get(URL).json()['friendlist']['friends']
# steamidlist = []
# for friend in range(len(friendlist)):
#     steamidlist.append(friendlist[friend]['steamid'])
# print(steamidlist)


#scherm
root = Tk()
root.title('Steam Add-on Project')
root.state('iconic')
root.geometry('720x480')

#widgets
# name = Label(root, text=f'Naam:  {gamenaam}')
# release = Label(root, text=f'Release Date:   {releasedate}')
# developer = Label(root, text=f'Developer:   {developer}')
# price = Label(root, text=f'Prijs:   {prijs}')
# achievement = Label(root, text= f'Achievements: {achievements}')
# platform = Label(root, text=f'Platforms:    {platforms}')
gamedata = Label(root, text=f'User stats:   {user_game_data}')

#plaatsing
# name.grid(row=0, column=0, sticky='w')
# release.grid(row=1, column=0, sticky='w')
# developer.grid(row=2, column=0, sticky='w')
# price.grid(row=3, column=0, sticky='w')
# achievement.grid(row=4, column=0, sticky='w')
# platform.grid(row=5, column=0, sticky='w')
gamedata.grid(row=6, column=4,sticky='w')
root.mainloop()
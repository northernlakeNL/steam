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
import webbrowser
global game_code
global URL


#values
API_key = 'AF90EFF02499BB3CDDFFF28629DEA47B'
# user_ID = '76561198084867313'
#json bestand uitlezen
with open('steam.json') as Steam:
    gamelist = json.load(Steam)

def clicked():                     #Clicked function
    game_name = receive_game_entry.get()
    Username = receive_steam_id.get()
    URL2= f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={API_key}&vanityurl={Username}'
    response = urlopen(URL2)
    user_data = json.loads(response.read())
    if user_data["response"]["success"] == '42':
        error_label = Label(root, text='Name not found')
        error_label.pack()
    else:
        steam_id = user_data["response"]["steamid"]
    for game in gamelist:
        if game["name"] == game_name:
            game_code = game['appid']
            name = game['name']
            release_date = game['release_date']
            price = game['price']
            achievements = game['achievements']
            developer = game['developer']
            platforms = game['platforms']
            URL = f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={game_code}&key={API_key}&steamid={steam_id}'
            response = urlopen(URL)
            user_game_data = json.loads(response.read())
            user_game_data_nice = json.dumps(user_game_data, indent=4, sort_keys=True)
            label1 = Label(root, text=f'game-ID: {game_code} \n game-naam:   {name} \n game-prijs:   {price} \n \n Your Data: \n {user_game_data_nice}')
            label1.pack()
            scrolling_hating = Scrollbar(root)
            scrolling_hating.pack(side= RIGHT, fill=Y)
            scrolling_hating.config(command = user_game_data_nice.yview )


#scherm
root = Tk()
root.title('Steam Add-on Project')
root.state('iconic')
root.geometry('720x480')

#widgets            
text_game_label = Label(root, text='Voor game naam in:')
text_game_label.pack()

receive_game_entry = Entry(root, width=40)
receive_game_entry.pack(padx=5, pady=5)

receive_Username = Label(root, text='Voor steam naam in:')
receive_Username.pack()

receive_steam_id = Entry(root, width=50)
receive_steam_id.pack(padx=5, pady=5)

send_game_button = Button(root, text='Press', bg='grey', command=clicked)
send_game_button.pack()

#URL compleet
# URL = f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={game_code}&key={API_key}&steamid={user_ID}'

root.mainloop()
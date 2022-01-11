import PySimpleGUI as sg
import os.path
import json
from urllib.request import urlopen
import time
import requests

API_key = 'AF90EFF02499BB3CDDFFF28629DEA47B'
game_list = []
game_list.clear
game_data = []
game_data.clear

# http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=240&key=AF90EFF02499BB3CDDFFF28629DEA47B&steamid=76561198084867313
    
User_column = [
    [
        sg.Text('Username: '),
        sg.Input(size=(20,1), key='_USER_'),
        sg.Button('Search')
    ],
]

file_list_column = [
    [
        sg.Text('Search Game: ', size=(15,1)), 
        sg.Input(do_not_clear=True, size=(20,1),enable_events=True, key='_INPUT_'),
    ],
    [        sg.Listbox(values=game_list, enable_events=True, size=(55,20), key='_LIST_')
],
]

game_data_column = [
    [
        sg.Text("Game data will be displayed here:")
    ],
    [
        sg.Text(size=(15,1), key="_TOUT_")
        ],
    [
        sg.Listbox(values=game_data, enable_events=True, size=(55,20), key='_DATA_')
        ]
]

layout = [
    [ 
        sg.Column(User_column),
        sg.VSeperator(),
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(game_data_column),
    ]
]

window = sg.Window("game info", layout)

#functies

def userinfo(username):
    global steam_id
    global URL2
    URL= f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={API_key}&vanityurl={username}'
    response1 = urlopen(URL)
    user_data = json.loads(response1.read())
    if user_data["response"]["success"] == 1:
        steam_id = user_data['response']['steamid']
        URL2= f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_key}&steamid={steam_id}&format=json&include_appinfo=1"
    else:
        sg.popup_error('User does not exist')

def game_info():
    global game_library
    global game_name
    x=0
    response5 = urlopen(URL2)
    game_list.clear()
    game_library = json.loads(response5.read())
    for game in game_library["response"]["games"]:
        if game["playtime_forever"] != 0:
            game_list.append(game["name"])
            x +=1
    window.Element('_LIST_').Update(game_list)

def achievements(appid):
    URL3=f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={appid}&key={API_key}&steamid={steam_id}'
    URL4=f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={appid}&format=json'
    achieved = 0
    to_achieve = 0
    r = requests.get(URL3)
    response3 = r.status_code
    try:
        if response3 == 200:
            window.Element('_DATA_').Update('')
            achievement_user = r.json() 
            if achievement_user['playerstats']['achievements']:
                for x in achievement_user['playerstats']['achievements']:
                    achieved +=1
                response4 = requests.get(URL4)
                achievement_all = response4.json()
            for x in achievement_all['achievementpercentages']['achievements']:
                to_achieve +=1
                progress = achieved / to_achieve
                percentage = progress * 100
                game_data.clear()
                game_data.append(game_name)
                game_data.append(percentage)
                window.Element('_DATA_').Update(game_data)
        if response3 == 400:
            window.Element('_DATA_').Update('')
            NA = "Not Available"
            game_data.clear()
            game_data.append(game_name)
            game_data.append(NA)
            window.Element('_DATA_').Update(game_data)
    except KeyError:
        window.Element('_DATA_').Update('')
        NA = "Not Available"
        game_data.clear()
        game_data.append(game_name)
        game_data.append(NA)
        window.Element('_DATA_').Update(game_data)

def game_id(name):
    global game_name
    global response2
    response2 = requests.get(URL2)
    library = response2.json()
    for game in library['response']['games']:
        if name == game['name']:
            game_name = game['name'] 
            game_data.append(game_name)
            app_id = game["appid"]
            print(app_id)               #WEG HALEN ALS ALLES WERKT
            achievements(app_id)

global last_search
global last_list
last_search = ""
last_list = []
while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if values['_INPUT_'] != '':
        search = values['_INPUT_']
        if search.startswith(last_search):
            last_list = [x for x in last_list if last_search in x]
        else:
            last_list = [x for x in game_list if last_search in x]
        window.Element('_LIST_').Update(last_list)
        last_search = search
    else:
        window.Element('_LIST_').Update(game_list)
    if event == '_LIST_':
        app_name = values['_LIST_']
        game_name = str(app_name[0])
        game_id(game_name)
        window.Element('_DATA_').Update(game_data)
    if values['_USER_'] != '':
        username= values['_USER_']
        userinfo(username)
        game_info()

window.close()
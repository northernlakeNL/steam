import PySimpleGUI as sg
import os.path
import json
from urllib.request import urlopen
import time

API_key = 'AF90EFF02499BB3CDDFFF28629DEA47B'

game_list = []

with open('steam.json') as steam:
    list2= json.load(steam)
    # max_achievements = list2['name']['achievements']


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
        sg.Listbox(values=game_list, enable_events=True, size=(55,20), key='_LIST_')
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

def userinfo():
    global steam_id
    global URL2
    URL= f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={API_key}&vanityurl={username}'
    response = urlopen(URL)
    user_data = json.loads(response.read())
    if user_data["response"]["success"] == 1:
        steam_id = user_data['response']['steamid']
        URL2= f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_key}&steamid={steam_id}&format=json&include_appinfo=1"
    else:
        sg.popup_error('User does not exist')

def game_info():
    global appid
    global game_library
    x=0
    response = urlopen(URL2)
    game_list.clear()
    game_library = json.loads(response.read())
    for game in game_library["response"]["games"]:
        game_list.append(game["name"])
        # appid = game["appid"]
        x +=1
    window.Element('_LIST_').Update(game_list)

def achievenments():
    appid = game_library["response"]["games"]["appid"]
    URL3=f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={appid}&key={API_key}&steamid={steam_id}'
    URL4=f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={appid}&format=json'
    achieved = 0
    to_achieve = 0
    response = urlopen(URL3)
    achievement_temp = json.loads(response.read())
    for x in achievement_temp['playerstats']['achievements']:
        achieved +=1
    response2 = urlopen(URL4)
    achievement_all = json.loads(response2.read())
    for x in achievement_all['achievementpercentages']['achievements']:
        to_achieve +=1
    progress = achieved / to_achieve
    percentage = progress * 100
    


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
    if event == '_LIST_' and len(values['_LIST_']):
        sg.Popup('Selected ', values['_LIST_'])
        achievenments()
    if values['_USER_'] != '':
        username= values['_USER_']
        userinfo()
        game_info()

window.close()


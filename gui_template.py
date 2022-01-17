import PySimpleGUI as sg
import os.path
import json
from urllib.request import urlopen
import time
from PySimpleGUI.PySimpleGUI import ProgressBar
import requests

API_key = 'AF90EFF02499BB3CDDFFF28629DEA47B'
game_list = []
game_list.clear
game_data = []
game_data.clear
tempo = []

# http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=240&key=AF90EFF02499BB3CDDFFF28629DEA47B&steamid=76561198084867313
    
# Het scherm

User_column = [
    [sg.Text('Username: '),
        sg.Input(size=(25,20), key='_USER_'),
        sg.Button('Search')],
]

file_list_column = [
    [sg.Text('Search Game: ', size=(15,1)), 
        sg.Input(do_not_clear=True, size=(20,1),enable_events=True, key='_INPUT_'),],
    [sg.Listbox(values=game_list, enable_events=True, size=(55,40), key='_LIST_')],
]

game_data_column = [
    [sg.vtop(sg.Text("Game data will be displayed here:"),
        sg.Text(size=(15,1), key="_TOUT_"))],
    [sg.vtop(sg.Listbox(values=game_data, enable_events=True, size=(55,20), key='_DATA_'))]
    # [sg.Graph()]
]

temp = [
    [sg.vbottom(sg.Listbox(values=tempo, enable_events=True, size=(55,20),  key='_GRAPH_'))]
]

layout = [
    [ sg.Column(User_column),
        sg.VSeperator(),
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(game_data_column),
        sg.HSeparator(),
        sg.Column(temp)
]]

window = sg.Window("game info", layout,size=(1280,720))

#functies

def userinfo(username):         # User info krijgen uit de steam API
    global steam_id
    URL= f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={API_key}&vanityurl={username}'
    response1 = urlopen(URL)
    user_data = json.loads(response1.read())
    if user_data["response"]["success"] == 1:
        steam_id = user_data['response']['steamid']
    else:
        sg.popup_error('User does not exist')

def game_info():            # Alles games van de User verzamelen en in een lijst stoppen
    global game_library
    global game_name
    global URL2
    x=0
    URL2= f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_key}&steamid={steam_id}&format=json&include_appinfo=1"
    response5 = urlopen(URL2)
    game_list.clear()
    game_library = json.loads(response5.read())
    for game in game_library["response"]["games"]:
        if game["playtime_forever"] != 0:
            game_list.append(game["name"])
            x +=1
    game_list.sort()
    window.Element('_LIST_').Update(game_list)

def achievements(appid):    # Behaalde achievement percentage van de aangeklikte game verzamalen 
    global percentage
    global URL3
    global URL4
    global game_data
    global percentage
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
                p = progress * 100
                percentage = f'Behaald: {round(p, 2)}%'
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
            spel = game['name']
            game_name = f'game:     {spel}'
            game_data.append(game_name)
            app_id = game["appid"]
            achievements(app_id)
        play_time(game_name)

def play_time(name):
    library = response2.json()
    # for game in library['response']['games']:
    #     if game == name:


global last_search
global last_list
last_search = ""
last_list = []
while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if values['_USER_'] != '':
        username= values['_USER_']
        userinfo(username)
        game_info()
    if values['_INPUT_'] != '':
        search = values['_INPUT_']
        if search.startswith(last_search):
            last_list = [x for x in game_list if last_search in x]
        else:
            last_list = [x for x in game_list if last_search in x]
        last_search = search
        print(last_list)
        window.Element('_LIST_').update(last_list)  
    if event == '_LIST_':
        app_name = values['_LIST_']
        game_name = str(app_name[0])
        game_id(game_name)
        window.Element('_DATA_').Update(game_data)
        window.Element('_GRAPH_').Update(tempo)

window.close()
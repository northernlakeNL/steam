import PySimpleGUI as sg
import os.path
import json
from urllib.request import urlopen

API_key = 'AF90EFF02499BB3CDDFFF28629DEA47B'

#functies

def userinfo():
    URL1= f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={API_key}&vanityurl={username}'
    response = urlopen(URL1)
    user_data = json.loads(response.read())
    if user_data["response"]["success"] == '42':
        sg.popup_error('User does not exist')
    else:
        steam_id = user_data['response']['steamid']
        print(steam_id)

with open('steam.json') as steam_data:
    data1 = json.loads(steam_data.read())

game_list = []
x = 0
for game in data1:
    game_list.append(data1[x]['name'])
    x +=1

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
    [
        sg.Listbox(values=game_list, enable_events=True, size=(40,20), key='_LIST_')
    ],
]

image_viewer_column = [
    [sg.Text("Game data will be displayed here:")],
    [sg.Text(size=(40,1), key="_TOUT_")],
    [sg.Image(key="_IMAGE_")]
]

layout = [
    [ 
        sg.Column(User_column),
        sg.VSeperator(),
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("User Info", layout)

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if values['_INPUT_'] != '':
        search = values['_INPUT_']
        new_values = [x for x in game_list if search in x]
        window.Element('_LIST_').Update(new_values)
    else:
        window.Element('_LIST_').Update(game_list)
    if event == '_LIST_' and len(values['_LIST_']):
        sg.Popup('Selected ', values['_LIST_'])
    if values['_USER_'] != '':
        username= values['_USER_']
        userinfo()

window.close()
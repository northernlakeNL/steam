import PySimpleGUI as sg
import os.path
import json

with open('steam.json') as steam_data:
    data1 = json.loads(steam_data.read())

game_list = []
x = 0
for game in data1:
    game_list.append(data1[x]['name'])
    x +=1

file_list_column = [
    [
        sg.Text('Search Game: '),
        sg.Input(do_not_clear=True, size=(20,1),enable_events=True, key='_INPUT_'),
    ],
    [
        sg.Listbox(
            values=game_list, enable_events=True, size=(40,20),
            key="_LIST_"
        )
    ],
]

image_viewer_column = [
    [sg.Text("Game data will be displayed here:")],
    [sg.Text(size=(40,1), key="_TOUT_")],
    [sg.Image(key="_IMAGE_")]
]

layout = [
    [ 
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
        sg.Popup('Selected ', data1['achievements'])
window.close()
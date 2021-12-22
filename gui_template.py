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

# print(game_list)

file_list_column = [
    [
        sg.Text(),
        sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
    ],
    [
        sg.Listbox(
            values=[game_list], enable_events=True, size=(40,20),
            key="-FILE LIST-"
        )
    ],
]

image_viewer_column = [
    [sg.Text("Game data will be displayed here:")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")]
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
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)

    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass
window.close()
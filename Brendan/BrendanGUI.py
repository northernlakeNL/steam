import threading
from turtle import xcor
import PySimpleGUI as sg
import json
from urllib.request import urlopen
from PySimpleGUI.PySimpleGUI import ProgressBar
import requests
import math
from matplotlib import pyplot as plt
# import sshpi

API_key = 'AF90EFF02499BB3CDDFFF28629DEA47B'
game_list = []
game_data = []
tempo = []
percentage = 0
gen_list = []
# http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={AF90EFF02499BB3CDDFFF28629DEA47B}&steamid={76561198172219198}&format=json&include_appinfo=1
# http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=240&key=AF90EFF02499BB3CDDFFF28629DEA47B&steamid=76561198084867313

def genres():
    global steam_id
    URL1 = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_key}&steamid=NL_Northie&format=json&include_appinfo=1"
    response_gamedata_url_1 = urlopen(URL1)
    data1 = json.loads(response_gamedata_url_1.read())
    appidlst = []
    for gameid in data1["response"]["games"]:
        appid = gameid['appid']
        appidlst.append(appid)
    print(appidlst)

# genres()


# ----------------------------------------------------------------- Grafieken van steamdata (matplotlib) ------------------------------------------------

def graph_values():
    global steam_id
    URL_APPID = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_key}&steamid={steam_id}&format=json&include_appinfo=1"
    response_gamedata = urlopen(URL_APPID)
    game_library = json.loads(response_gamedata.read())
    time_list = []
    x = 0
    x_axis = ['']                                           #lst van de games
    y_axis = [0]                                            #lst van de uren
    for game in game_library["response"]["games"]:
        if game["playtime_forever"] != 0:
            time_list.append(game["playtime_forever"])
            time_list.sort()
    for x in range(len(time_list)-10, len(time_list)):      # Tijden met games samen voegen voor de lijst
        for game in game_library["response"]["games"]:
            if time_list[x] == game["playtime_forever"]:
                if game["playtime_forever"] >= 60:
                    hours = (game["playtime_forever"] // 60)               # Minuten in uren zetten
                    minutes = round(((game["playtime_forever"] // 60) - hours) * 60) # Overige weer terug zetten in minuten
                    if minutes < 10:
                        minutes = f'0{minutes}'
                    play_time = f'{hours}:{minutes}'
                else:
                    play_time = game["playtime_forever"]
                x_axis.append(game["name"])
                y_axis.append(hours)
    plt.xticks(rotation=90)
    plt.barh(x_axis, y_axis, label='Time')
    plt.title("Mosted played games"), plt.xlabel("hours"), plt.ylabel("Games")
    plt.ylim(ymin=0)
    plt.legend()
    mng = plt.get_current_fig_manager()         #Fullscreen plt show
    mng.window.state('zoomed')                  #Fullscreen plt show
    plt.show()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

User_column = [                                             # De eerste Colom waar de gebruikersnaam kan worden ingevuld en de algemen data komt
    [   sg.vtop(sg.Text('Username: ')),
        sg.vtop(sg.Input(size=(25,20), key='_USER_')),
        sg.vtop(sg.Button('Search')),
        ],
    [sg.Listbox(values=gen_list, enable_events=True, size=(55,20), k='_GENERAL_')],
    [sg.vbottom(sg.Text("Grafiek van je meest gespeelde games"))],
    [sg.vbottom(sg.Button("Press", key='-input-'))],
]

file_list_column = [                                        # De gebruikers bibliotheek weergeven met een zoek functie
    [sg.Text('Search Game: ', size=(10,1)),
        sg.Input(do_not_clear=True, size=(30,1),enable_events=True, key='_INPUT_'),],
    [sg.Listbox(values=game_list, enable_events=True, size=(55,40), key='_LIST_')],
]

game_data_column = [                                        # Alle game data van de aangeklikte game weergeven
    [sg.vtop(sg.Text("Game data will be displayed here:"),
        sg.Text(size=(15,1), key="_TOUT_"))],  # doet dit iets? - M.K.
    [sg.vtop(sg.Listbox(values=game_data, enable_events=True, size=(55,20), expand_x=True, expand_y=True, key='_DATA_'))],
    [sg.vbottom(sg.Listbox(values=tempo, enable_events=True, size=(55,20),  key='_GRAPH_'))]
]

layout = [                                                  # volgorde van de layout van links naar rechts
    [ sg.Column(User_column),
        sg.VSeperator(),
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(game_data_column),
]]

window = sg.Window("game info", layout,element_justification='center', resizable=True, finalize=True)
window.Maximize()
window.finalize()
window['_LIST_'].expand(True, True, True)
#functies

def userinfo(username):         # User info krijgen uit de steam API
    global steam_id
    if username.isdecimal():    # kan nu ook volledige steamid invullen (voor brendan enzo)
        steam_id = username
        gen_data()
    else:
        URL= f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={API_key}&vanityurl={username}'
        response1 = urlopen(URL)
        user_data = json.loads(response1.read())
        if user_data["response"]["success"] == 1:               # User opzoeken
            steam_id = user_data['response']['steamid']
            gen_data()
        else:
            sg.popup_error('User does not exist')

def gen_data():                 # Algemene Data zoals meest gespeelde games + tijden
    global gen_list
    time_list = []
    x = 0
    URL2= f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_key}&steamid={steam_id}&format=json&include_appinfo=1"
    response5 = urlopen(URL2)
    game_library = json.loads(response5.read())
    gen_list.clear()                                        # Herhaaldelijk inladen voorkomen
    try:
        for game in game_library["response"]["games"]:
            if game["playtime_forever"] != 0:
                time_list.append(game["playtime_forever"])
                time_list.sort()
        for x in range(len(time_list)-10, len(time_list)):      # Tijden met games samen voegen voor de lijst
            for game in game_library["response"]["games"]:
                if time_list[x] == game["playtime_forever"]:
                    if game["playtime_forever"] >= 60:
                        hours = (game["playtime_forever"] // 60)               # Minuten in uren zetten
                        minutes = round(((game["playtime_forever"] // 60) - hours) * 60) # Overige weer terug zetten in minuten
                        if minutes < 10:
                            minutes = f'0{minutes}'
                        play_time = f'{hours}:{minutes}'
                    else:
                        play_time = game["playtime_forever"]
                    gen_list.append(f'{game["name"]}, {play_time}')
        window.Element('_GENERAL_').Update(gen_list)
        game_info()
    except KeyError:
        sg.popup_error("Game list not available\n(Maybe multiple users share that name?)")

def game_info():            # Alles games van de User verzamelen en in een lijst stoppen
    global game_library
    global game_name
    global URL2
    global playtime
    x=0
    URL2= f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_key}&steamid={steam_id}&format=json&include_appinfo=1"
    response5 = urlopen(URL2)
    game_list.clear()
    game_library = json.loads(response5.read())
    for game in game_library["response"]["games"]:      # Lijst van alle games van de gebruiker
        game_list.append(game["name"])
        x +=1
    game_list.sort()
    # graph_values()                                          #Runned graph function
    window.Element('_LIST_').Update(game_list)

def achievements(appid, playtime):      # Behaalde achievement percentage van de aangeklikte game verzamalen
    global percentage
    global URL3
    global URL4
    global game_data
    global percentage
    URL3=f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={appid}&key={API_key}&steamid={steam_id}'
    URL4=f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={appid}&format=json'
    achieved = 0
    to_achieve = 0
    progress = 0
    r = requests.get(URL3)
    response3 = r.status_code
    try:
        if response3 == 200:                                # Response code check (positief)
            window.Element('_DATA_').Update('')
            achievement_user = r.json()
            if achievement_user['playerstats']['achievements']:         # Achievements opzoeken van de gebruiker
                for x in achievement_user['playerstats']['achievements']:
                    achieved +=1
                response4 = requests.get(URL4)
                achievement_all = response4.json()
            for x in achievement_all['achievementpercentages']['achievements']: # Alle beschikbare Achievements opzoeken van het spel
                to_achieve +=1
                progress = achieved / to_achieve
                p = progress * 100
                percentage = f"behaald:     {round(p, 2)}%"
                game_data.clear()
                game_data.append(game_name)
                game_data.append(playtime)
                game_data.append(percentage)
                window.Element('_DATA_').Update(game_data)
            #threading.Thread(target=sshpi.ledbalk, args=(int(progress*100),)).start()
        if response3 == 400:                                # Response code check (negatief)
            window.Element('_DATA_').Update('')
            NA = "Not Available"
            game_data.clear()
            game_data.append(game_name)
            game_data.append(playtime)
            game_data.append(NA)
            window.Element('_DATA_').Update(game_data)
    except KeyError:                                        # Als er geen Achievements zijn
        window.Element('_DATA_').Update('')
        NA = "Not Available"
        game_data.clear()
        game_data.append(game_name)
        game_data.append(playtime)
        game_data.append(NA)
        window.Element('_DATA_').Update(game_data)

def game_id(name):                      # App ID met playtime opzoeken
    global game_name
    global response2
    response2 = requests.get(URL2)
    library = response2.json()
    for game in library['response']['games']:
        if name == game['name']:
            spel = game['name']
            game_name = f'game:         {spel}'
            game_data.append(game_name)
            app_id = game["appid"]
            if game["playtime_forever"] >= 60:
                hours = math.floor(game["playtime_forever"] / 60)
                minutes = round(((game["playtime_forever"] / 60) - hours) * 60)
                if minutes < 10:
                    minutes = f'0{minutes}'
                playtime = f'playtime:     {hours}h:{minutes}m'
            else:
                playtime = f'{game["playtime_forever"]}m'
            achievements(app_id, playtime)

while True:
    event, values = window.Read()
    last_search = ""
    last_list = []
    if event is None or event == 'Exit':            # Afsluiten van het programma zonder Errors
        break
    if values['_USER_'].strip() != '' and ' ' not in values['_USER_'].strip():                      # User opzoeken
        username= values['_USER_']
        userinfo(username)
    if values['_INPUT_'] != '':                     # Live search in library
        search = values['_INPUT_']
        if search.startswith(last_search):
            last_list = [x for x in game_list if last_search in x]
        else:
            last_list = [x for x in game_list if last_search in x]
        last_search = search
        print(last_list)
        window.Element('_LIST_').update(last_list)
    if event == '_LIST_':                           # Library in de GUI verwerken
        app_name = values['_LIST_']
        game_name = str(app_name[0])
        game_id(game_name)
        window.Element('_DATA_').Update(game_data)
    if event == '-input-':
        graph_values()
window.close()
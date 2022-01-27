
#-------------------------------------------------IMPORTS-------------------------------------------------#
from nturl2path import url2pathname
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

#-------------------------------------------------PRE-VALUES-------------------------------------------------#
API_key = 'AF90EFF02499BB3CDDFFF28629DEA47B'
game_list = []
game_data = []
tempo = []
percentage = 0
gen_list = []

#-------------------------------------------------COLUMNS-------------------------------------------------#
user_column = [                                             # De eerste Colom waar de gebruikersnaam kan worden ingevuld en de algemen data komt
    [(sg.Text('Username: ')),
     (sg.Input(size=(25,20), key='_USER_')),
     (sg.Button('Search'))
     ],
    [sg.Listbox(values=gen_list, enable_events=True, size=(55,20), k='_GENERAL_')],
    # [sg.vbottom(sg.Text("Grafiek van je meest gespeelde games"))],
    # [sg.vbottom(sg.Button("Press", key='-input-'))],
    ]

file_list_column = [                                        # De gebruikers bibliotheek weergeven met een zoek functie
    [sg.Text('Search Game: ', size=(10,1)),
     sg.Input(do_not_clear=True, size=(30,1),enable_events=True, key='_INPUT_'),
     ],
    [sg.Listbox(values=game_list, enable_events=True, size=(55,20), key='_LIST_')],]

game_data_column = [                                        # Alle game data van de aangeklikte game weergeven
    [(sg.Text("Game data will be displayed here:")),],
    [(sg.Listbox(values=game_data, enable_events=True, size=(55,20), expand_x=True, expand_y=True, key='_DATA_'))],
    ]

#-------------------------------------------------TABS-------------------------------------------------#

tab1_layout = [[sg.Listbox(values=gen_list, enable_events=True, size=(170,30), k='-input-')]]               # Verschillende tabs voor de unieke data
tab2_layout = [[sg.Listbox(values=gen_list, enable_events=True, size=(170,30), k='_GENERAL_')]] # GENERAL is een placeholder
tab3_layout = [[sg.Listbox(values=gen_list, enable_events=True, size=(170,30), k='_GENERAL_')]]
tab4_layout = [[sg.Listbox(values=gen_list, enable_events=True, size=(170,30), k='_GENERAL_')]]
tab5_layout = [[sg.Listbox(values=gen_list, enable_events=True, size=(170,30), k='_GENERAL_')]]
tab6_layout = [[sg.Listbox(values=gen_list, enable_events=True, size=(170,30), k='_GENERAL_')]]

tab_group_layout = [[sg.Tab('Time Graph', tab1_layout, font='Courier 15', key='-TAB1-', expand_x=True),
                     sg.Tab('Genre Graph', tab2_layout, font='Courier 15', key='-TAB2-', expand_x=True),
                     sg.Tab('Time per Genre', tab3_layout, font='Courier 15', key='-TAB2-', expand_x=True),
                     sg.Tab('Achievements per Genre', tab4_layout, font='Courier 15', key='-TAB2-', expand_x=True),
                     sg.Tab('User Data', tab5_layout, font='Courier 15', key='-TAB2-', expand_x=True),
                     sg.Tab('CS:GO Stats', tab6_layout, font='Courier 15', key='-TAB2-', expand_x=True),
                     ]]

#-------------------------------------------------LAYOUT-------------------------------------------------#

layout = [                                            # volgorde van de layout van links naar rechts
            [sg.Frame(layout= user_column, title='', border_width=0, vertical_alignment='top'),
             sg.Frame(layout= file_list_column, title='', border_width=0, vertical_alignment='top'),
             sg.Frame(layout= game_data_column, title='', border_width=0, vertical_alignment='top'),],
            [sg.TabGroup(layout= tab_group_layout, enable_events=True,)]
            ]

window = sg.Window("Victis-Victis Add-On", layout, size=(1280, 960), element_justification='center', resizable=True, finalize=True)
# window.Maximize()
# window.finalize()
window['_LIST_'].expand(True, True, True)


#-------------------------------------------------FUNCTIONS-------------------------------------------------#

#--------URL Functies--------#
def URL1(username):
    URL1    =   f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={API_key}&vanityurl={username}'
    return URL1
def URL2(steam_id):
    URL2    =   f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_key}&steamid={steam_id}&format=json&include_appinfo=1"
    return URL2
def URL3(appid, steam_id):
    URL3    =   f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={appid}&key={API_key}&steamid={steam_id}'
    return URL3
def URL4(appid):
    URL4    =   f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={appid}&format=json'
    return URL4

def graph_values(game_library):
    time_list = []
    x = 0
    x_axis = ['']                                           #lst van de games
    y_axis = [0]                                            #lst van de uren
    play_stat = time(game_library)
    for x in play_stat:
        new_x = x.split(';')
        x_axis.append(new_x[0])
        y_axis.append(float(new_x[3]))
    plt.xticks(rotation=90)
    plt.barh(x_axis, y_axis, label='Time')
    for i, v in enumerate(y_axis):
        plt.text(v+0.1, i + 0, str(str(round(int(v), 0))), color='black')
    plt.title("Mosted played games"), plt.xlabel("hours"), plt.ylabel("Games")
    plt.ylim(ymin=0)
    plt.legend()
    mng = plt.get_current_fig_manager()         #Fullscreen plt show
    mng.window.state('zoomed')                  #Fullscreen plt show
    plt.show()

def genres(game_list):
    global tagsdict
    steam_json = open('C:/Users/tomno/Documents/GitHub/steam/Tom/steam.json', 'r')            # steam json lijst
    steam_list = json.loads(steam_json.read())
    genre = open('C:/Users/tomno/Documents/GitHub/steam/Tom/popular_genres.txt', 'r+')        # lijst met genre/tags
    appidlst = []
    tagsdict = {}
    y=0
    genre_list = []
    for x in genre:                          #in een genre pythonlijst zetten                                                 
        genre_list.append(x)
    genre_list.sort()
    genre.close()
    for genre in genre_list:              #lijst in een Dictionary zetten
        tagsdict[genre[:-1]]=y
    for gameid in game_list["response"]["games"]:       # app id lijst van de gebruiker opvragen
        appid = gameid["appid"]
        appidlst.append(appid)
        appidlst.sort()
    for id in appidlst:              
        for value in steam_list:               
            if id == value["appid"]:               # checken if id van appidlst gelijk is aan een appid
                for game in steam_list:               
                    if id == game["appid"]:               # als de appid gelijk is
                        tag = game["steamspy_tags"]               # de steam tags pakken
                        tag_list = tag.split(";")               # tags opsplitsen
                        for tag in tag_list:               
                            if tag in tagsdict:               # checken of tag in tagsdict staat
                                tagsdict[tag] = tagsdict[tag] + 1               # tag +1 value geven
                            else:
                                tagsdict[tag] = 1               # tag toevoegen aan dictionary en een waarde van 1 geven
                                genre_list.append(tag)               # tag toevoegen aan genre_list
                                with open('C:/Users/tomno/Documents/GitHub/steam/Tom/popular_genres.txt', 'a') as add_genre:
                                    add_genre.write(f'\n{tag}')               # tag toevoegen aan alle bekende tags/genres
    tagslst = []
    for key, val in tagsdict.items():
        key = key.replace(" ", "_")               # spaties vervangen voor '_'
        if val >= 1:
            if val <10:
                val = f'0{val}'               # als de waarde lager dan 10 is een 0 voor het cijfer toevoegen
                tagslst.append(f'{val}:     {key}')               # nieuwe waare toeveoegen in lijst
                tagslst.sort(reverse= True)          
            else:
                tagslst.append(f'{val}:     {key}')               # waarde toevoegen aan lijst
    tagslst.sort(reverse= True)                      
    window.Element('_GRAPH_').Update(tagslst)

def time(game_library):
    most_played = []
    time_list = []
    for game in game_library["response"]["games"]:
        if game["playtime_forever"] != 0:
            time_list.append(game["playtime_forever"])
            time_list.sort()
    for x in range(len(time_list)-10, len(time_list)):      # Tijden met games samen voegen voor de lijst
        for game in game_library["response"]["games"]:
            name = game["name"]
            if time_list[x] == game["playtime_forever"]:
                if game["playtime_forever"] >= 60:
                    hours = (game["playtime_forever"] // 60)               # Minuten in uren zetten
                    minutes = (((game["playtime_forever"] // 60) - hours) * 60) # Overige weer terug zetten in minuten
                    p_time = (game["playtime_forever"] / 60) 
                    play_time = round(p_time, 2)
                    most_played.append(f'{name};{hours};{minutes};{play_time}')
                else:
                    most_played.append(f'{name};{game["playtime_forever"]}') 
    return most_played

def userinfo(username):         # User info krijgen uit de steam API
    global steam_id
    if username.isdecimal():    # kan nu ook volledige steamid invullen (voor brendan enzo)
        steam_id = username
        return gen_data()
    else:
        URL = URL1(username)
        response1 = urlopen(URL)
        user_data = json.loads(response1.read())
        if user_data["response"]["success"] == 1:               # User opzoeken
            steam_id = user_data['response']['steamid']
            return gen_data()
        else:
            sg.popup_error('User does not exist')

def gen_data():                 # Algemene Data zoals meest gespeelde games + tijden
    global gen_list
    time_list = []
    x = 0
    URL= URL2(steam_id)
    response5 = urlopen(URL)
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
                        hours = math.floor(game["playtime_forever"] / 60)               # Minuten in uren zetten
                        minutes = round(((game["playtime_forever"] / 60) - hours) * 60) # Overige weer terug zetten in minuten
                        if minutes < 10:
                            minutes = f'0{minutes}'
                        play_time = f'{hours}:{minutes}'
                    else:
                        play_time = game["playtime_forever"]
                    gen_list.append(f'{game["name"]}, {play_time}')
        window.Element('_GENERAL_').Update(gen_list)
        game_info(game_library)
        genres(game_library)
        return game_library
    except KeyError:
        sg.popup_error("Game list not available\n(Maybe multiple users share that name?)")

def game_info(game_library):            # Alles games van de User verzamelen en in een lijst stoppen
    global game_name
    global playtime
    x=0
    for game in game_library["response"]["games"]:      # Lijst van alle games van de gebruiker
        game_list.append(game["name"])
        x +=1
    game_list.sort()
    window.Element('_LIST_').Update(game_list)

def achievements(appid, playtime):      # Behaalde achievement percentage van de aangeklikte game verzamalen
    global percentage
    global game_data
    global percentage
    URL1= URL3(steam_id)
    URL2= URL4(steam_id)
    achieved = 0
    to_achieve = 0
    progress = 0
    r = requests.get(URL1)
    response3 = r.status_code
    try:
        if response3 == 200:                                # Response code check (positief)
            window.Element('_DATA_').Update('')
            achievement_user = r.json()
            if achievement_user['playerstats']['achievements']:         # Achievements opzoeken van de gebruiker
                for x in achievement_user['playerstats']['achievements']:
                    achieved +=1
                response4 = requests.get(URL2)
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
    global game_library
    response2 = requests.get(URL2)
    game_library = response2.json()
    for game in game_library['response']['games']:
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

#-------------------------------------------------value activaties-------------------------------------------------#

while True:
    event, values = window.Read()
    last_search = ""
    last_list = []
    if event is None or event == 'Exit':            # Afsluiten van het programma zonder Errors
        break
    if values['_USER_'].strip() != '' and ' ' not in values['_USER_'].strip():                      # User opzoeken
        username= values['_USER_']
        game_data = userinfo(username)
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
        graph_values(game_data)
window.close()
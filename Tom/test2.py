from nturl2path import url2pathname
import threading
from turtle import xcor
import PySimpleGUI as sg
import json
from urllib.request import urlopen
from PySimpleGUI.PySimpleGUI import ProgressBar
import matplotlib
from matplotlib.figure import Figure
import numpy as np
import requests
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import Figure
from github import Github

# def graph_genre_time():
#     steam_json = open('FINAL MAP\steam.json', 'r')
#     steam_list = json.loads(steam_json.read())
#     genre = open('FINAL MAP\popular_genres.txt', 'r+')
#     game_json = open('Tom\gamesTom.json', 'r')
#     game_list = json.loads(game_json.read())
#     genre_dict = {}
#     genre_dict.clear()
#     time_list= []
#     x_axis = ['']
#     y_axis = [0]
#     for x in genre:
#         x = x[:-1]
#         genre_dict[x] = 0
#     for y in game_list["response"]["games"]:
#         game_y = y
#         for x in steam_list:
#             game_x = x
#             if game_y['name'] == game_x['name']:
#                 if game_y['playtime_forever'] >= 1:
#                     z = game_x['steamspy_tags']
#                     z_split = z.split(';')
#                     for i in z_split:
#                         if i in genre_dict:
#                             genre_dict[i] = genre_dict[i] + game_y['playtime_forever']
#     for x in genre_dict:
#         if genre_dict[x] >= 1 and genre_dict[x] < 10:
#             time_list.append(f'0000000{genre_dict[x]}; {x}')
#         elif genre_dict[x] >= 10 and genre_dict[x] < 100:
#             time_list.append(f'000000{genre_dict[x]}; {x}')
#         elif genre_dict[x] >= 100 and genre_dict[x] < 1000:
#             time_list.append(f'00000{genre_dict[x]}; {x}')
#         elif genre_dict[x] >= 1000 and genre_dict[x] < 10000:
#             time_list.append(f'0000{genre_dict[x]}; {x}')
#         elif genre_dict[x] >= 10000 and genre_dict[x] < 100000:
#             time_list.append(f'000{genre_dict[x]}; {x}')
#         elif genre_dict[x] >= 100000 and genre_dict[x] < 1000000:
#             time_list.append(f'00{genre_dict[x]}; {x}')
#         elif genre_dict[x] >= 1000000 and genre_dict[x] < 10000000:
#             time_list.append(f'0{genre_dict[x]}; {x}')
#         elif genre_dict[x] >= 10000000 and genre_dict[x] < 100000000:
#             time_list.append(f'{genre_dict[x]}; {x}')
#     time_list.sort(reverse=False)
#     for x in time_list[-10:]:
#         new_x = x.split(';')
#         x_axis.append(new_x[1])
#         new_new_x = int(new_x[0]) // 60
#         y_axis.append(new_new_x)
#     plt.figure(figsize=(15, 7))
#     plt.tick_params(axis='y', which='major', labelsize=6)
#     plt.xticks(rotation=90)
#     plt.barh(x_axis, y_axis, label='Time')
#     for i, v in enumerate(y_axis):
#         if i > 0:
#             plt.text(v+0.1, i + 0, str(str(round(int(v), 0))), color='black')
#     plt.title("Mosted played games"), plt.xlabel("hours"), plt.ylabel("Games")
#     plt.ylim(ymin=0)
#     plt.legend()
#     fig = plt.gcf()     # een afbeelding maken van de grafiek
#     return fig
# graph_genre_time()

URL    =   f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=40800&key=AF90EFF02499BB3CDDFFF28629DEA47B&steamid=76561198084867313'

def genre_achievements(URL):
    appid_lst = []
    dictdict = {}
    steam_json = open('FINAL MAP\steam.json', 'r')  
    steam_list = json.loads(steam_json.read())
    genre = open('FINAL MAP\popular_genres.txt', 'r+') 
    game_json = open('Tom\gamesTom.json', 'r')
    game_list = json.loads(game_json.read())
    response5 = urlopen(URL)
    achievments = json.loads(response5.read())
    for y in game_list['response']['games']:
        if y['playtime_forever'] > 0:
            appid_lst.append(y['appid'])
    for x in genre:                                 #genre in dictionary zetten
        x = x[:-1]
        dictdict[x] = 0
    for y in game_list["response"]["games"]:            # games zoeken
        for x in steam_list:
            if y['name'] == 40800:        # tags van de game opzoeken
                if y['playtime_forever'] >= 1:
                    z = x['steamspy_tags']
                    z_split = z.split(';')
                    for i in z_split:
                        if i in dictdict:
                            for q in achievments['playerstats']['achievements']:
                                dictdict[i] = dictdict[i] + 1

    print(dictdict)
genre_achievements(URL)
from tkinter import *
from tkinter import ttk
import json
import os
import statistics
import pandas as pd
import numpy
import requests

S = open('steam.json')
gamedata = json.load(S)
with open('steam.json') as Steam:
    gamelist = json.load(Steam)

root = Tk() #Mainscherm

def clicked():                     #Clicked function
    game_name = receive_game_entry.get()
    for game in gamelist:
        if game["name"] == game_name:
            name = game['name']
            # release_date = game['release_date']
            # price = game['price']
            # achievements = game['achievements']
            # developer = game['developer']
            # platforms = game['platforms']

            label1 = Label(master=root, text=f'{name}')
            label1.pack()


text_game_label = Label(master=root, text='Voor game naam in:')
text_game_label.pack()

receive_game_entry = Entry(master=root, width=40)
receive_game_entry.pack(padx=5, pady=5)

send_game_button = Button(master=root, text='Press', bg='grey', command=clicked) #brendan is een kluns
send_game_button.pack()


root.mainloop()
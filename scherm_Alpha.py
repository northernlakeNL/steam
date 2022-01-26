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

#   Function place
def clicked():   #Gegevens ophalen functie
    game_naam = 'e'
    game_naam = gamesbalk.get()
    return game_naam
#   Function place

root = Tk()
root.title("Data")

gamesbericht = Label(master=root, text="Voer hier een game in waar je de statestieken over wilt weten") #text
gamesbericht.pack()

gamesbalk = Entry(master=root, width=50)    #Textbalk
gamesbalk.pack(padx=10, pady=10)

gamesbutton = Button(master=root, text='Verzend gegevens', command=clicked) #Button, gegevensophalen command. 
gamesbutton.pack(pady=3)

game_naam = clicked()

print(game_naam)

with open('steam.json') as Steam:
    gamelist = json.load(Steam)

for game in gamelist:
    if game["name"] == game_naam:
        name = game['name']
        release_date = game['release_date']
        price = game['price']
        achievements = game['achievements']
        developer = game['developer']
        platforms = game['platforms']
    
label1 = Label(master=root, text=name)
label1.pack()
label2 = Label(master=root, text=release_date)
label2.pack()
label3 = Label(master=root, text=price)
label3.pack()
label4 = Label(master=root, text=achievements)
label4.pack()
label5 = Label(master=root, text=developer)
label5.pack()
label6 = Label(master=root, text=platforms)
label6.pack()

root.mainloop()
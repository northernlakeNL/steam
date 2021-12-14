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

root = Tk()
root.title("Data")
#   Function place
def clicked(): #Gegevens ophalen functie
    naam = gamesbalk.get()
    test = Label(master=root, text=naam)
    test.pack()
#   Function place

gamesbericht = Label(master=root, text="Voer hier een game in waar je de statestieken over wilt weten")
gamesbericht.pack()

gamesbalk = Entry(master=root, width=50)
gamesbalk.pack(padx=10, pady=10)

gamesbutton = Button(master=root, text='Verzend gegevens', command=clicked)
gamesbutton.pack(pady=3)

root.mainloop()
#alle imports die nodig zijn
from tkinter import *
from tkinter import ttk
import json
import os
import statistics
import pandas as pd
import numpy
import requests
from urllib.request import urlopen
from time import sleep


API_key = 'AF90EFF02499BB3CDDFFF28629DEA47B'
user_ID = '76561198172219198'


scherm = Tk()
scherm.title('Steam Add-On project')
scherm.geometry('720x480')

label1 = Label(scherm,
                text= 'Game that you want')
label1.pack()

def get_data():
    test.config(text=""+text.get(1.0, "end-1c"))

text = Text(scherm,width=80, height=15)
text.insert(END, "")
text.pack()

knop = ttk.Button(scherm,
                text='Submit',
                command=get_data)
knop.pack()

test = Label(scherm, text="", font=18)
test.pack()

scherm.mainloop()
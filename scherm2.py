import tkinter as tk
from tkinter import ttk
import json
import os
import statistics
import pandas as pd
import numpy
import requests
S = open('steam.json')
gamedata = json.load(S)

root = tk.Tk()

root.title("Data")
# tabControl = ttk.Notebook(root) #tabfunctie

# tab1 = ttk.Frame(tabControl)    #frame 1
# tab2 = ttk.Frame(tabControl)    #frame 2

# tabControl.add(tab1, text='Tab 1')
# tabControl.add(tab2, text='Tab 2')

# tabControl.pack(expand=1, fill="both")

# ttk.Label(tab1, text='x').grid(column=0, row=0, padx=30, pady=30)                    #Label in frame 1
# ttk.Label(tab2, text='x').grid(column=0, row=0, padx=30, pady=30)       #Label in frame 2



root.mainloop()
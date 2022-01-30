#!/usr/bin/env python
import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
"""
Demonstrates one way of embedding Matplotlib figures into a PySimpleGUI window.

Paste your Pyplot code into the section marked below.

Do all of your plotting as you normally would, but do NOT call plt.show(). 
Stop just short of calling plt.show() and let the GUI do the rest.

The remainder of the program will convert your plot and display it in the GUI.
If you want to change the GUI, make changes to the GUI portion marked below.

"""

# ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE -------------------------------

values_to_plot = (20, 35, 30, 35, 57)
ind = np.arange(len(values_to_plot))
width = 0.4

p1 = plt.bar(ind, values_to_plot, width)

plt.ylabel('Y-Axis Values')
plt.title('Plot Title')
plt.xticks(ind, ('Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0],), ('Data Group 1',))


# ------------------------------- END OF YOUR MATPLOTLIB CODE -------------------------------

# ------------------------------- Beginning of Matplotlib helper code -----------------------

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# ------------------------------- Beginning of GUI CODE -------------------------------
sg.theme('Light Brown 3')

fig = plt.gcf()  # if using Pyplot then get the figure from the plot
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

tab1_layout = [[sg.Canvas(size=(170, 30), k='_TIME_GRAPH_')]]  
tab_group_layout = [[sg.Tab('Time Graph', tab1_layout, font='Courier 15', key='_TIME_GRAPH_', expand_x=True)]]


# define the window layout
layout = [[sg.Text('Plot test', font='Any 18')],
          [sg.Button('launch', k='-input-')],
          [sg.Canvas(size=(100, figure_h), key='-CANVAS-')],
          [sg.OK(pad=((figure_w / 2, 0), 3), size=(4, 2))],
          [sg.TabGroup(layout= tab_group_layout, enable_events=True,)]]

# create the form and show it without the plot
window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI',
    layout, force_toplevel=True, finalize=True,
    )

# add the plot to the window

# fig_photo = 

# show it all again and get buttons
while True:
    event, values = window.read()
    if event is None or event == 'Exit':            # Afsluiten van het programma zonder Errors
        break
    if event == '-input-':
        draw_figure(window['-CANVAS-'].TKCanvas, fig)

window.close()
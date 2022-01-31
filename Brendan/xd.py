import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg


matplotlib.use('TkAgg')
w, h = figsize = (15, 9)     # figure size
fig = matplotlib.figure.Figure(figsize=figsize)
dpi = fig.get_dpi()
size = (w*dpi, h*dpi)       # canvas size
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

layout = [[sg.Text('Plot test')],
          [sg.Canvas(size=size, key='-CANVAS-')],
          [sg.Button('Ok')]]

window = sg.Window('Embedding Matplotlib', layout, finalize=True, element_justification='center', font='Helvetica 18')
fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

event, values = window.read()

window.close()
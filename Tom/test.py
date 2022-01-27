import sys
import random
 
# Pass any command line argument for Web use
# if len(sys.argv) &gt 1: # if there is use the Web Interface
#     import PySimpleGUIWeb as sg
#     mode = "web"
#     mysize = (20,2)
 # default uses the tkinter GUI
import PySimpleGUI as sg
mode = "tkinter"
mysize = (12,1)
BAR_WIDTH = 150
BAR_SPACING = 175
EDGE_OFFSET = 3
GRAPH_SIZE = (500,500)
DATA_SIZE = (500,500)
 
bcols = ['blue','red','green']
myfont = "Ariel 18"
 
#update with your ip
myip = '192.168.0.107'
 
graph = sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE)
 
layout = [[sg.Text('Pi Sensor Values',font=myfont)],
  [graph],
  [sg.Text('PI Tag 1',text_color=bcols[0],font=myfont,size= mysize ),
  sg.Text('PI Tag 2',text_color=bcols[1],font=myfont,size= mysize ),
  sg.Text('PI Tag 3',text_color=bcols[2],font=myfont,size= mysize)],
  [sg.Exit()]]
 
if mode == "web":
    window = sg.Window('Real Time Charts', layout,web_ip=myip, web_port = 8888, web_start_browser=False)
else:
    window = sg.Window('Real Time Charts', layout)
while True:
    event, values = window.read(timeout=2000)
    if event in (None, 'Exit'):
        break
 
    graph.erase()
    for i in range(3):
# Random value are used. Add interface to Pi sensors here:
        graph_value = random.randint(0, 400)
        graph.draw_rectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, graph_value),
        bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0), fill_color=bcols[i])
        <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>graph.draw_text(text=str(graph_value), location=(i*BAR_SPACING+EDGE_OFFSET+15, graph_value+10),color=bcols[i],font=myfont)
 
window.close()
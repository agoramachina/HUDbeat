import time
import numpy as np
import pandas as pd
import plotext as plx
import recordEEG as eeg
import csv 

ymin = -1800
ymax = 1800
samples = 240

folder, file = eeg.get_recent(raw = True)

def get_raw():
  with open(file, "r") as f:
    tail = f.readlines()[-samples].strip().split('\t')[1]
  return(tail)

yticks = [-ymax, -ymax/2, 0, ymax/2, ymax]
ylabels = [-ymax, int(-ymax/2), "0 uV ", int(ymax/2), ymax]
#plx.yticks = (yticks, ylabels) 
plx.ylim = (-ymax, ymax) 


while True:
  data = get_raw()
  #print(data)
    

  #eeg.get_raw(samples)
  plx.clear_data()
  plx.clear_color()
  plx.frame(False)
  plx.grid(False)
  plx.xaxis(False)
  plx.yaxis(False)
  plx.xticks(None)
  plx.yticks(None)

  y=(data)
  #print(y)

  #yticks = [-ymax, -ymax/2, 0, ymax/2, ymax]
  #ylabels = [-ymax, int(-ymax/2), "0 µV ", int(ymax/2), ymax]
  #plx.yticks(yticks, ylabels)
  
  #plx.ylim(-ymax,ymax)
  plx.line(y, marker = "dot", color='white')
  #plx.clear_terminal()
  plx.show()

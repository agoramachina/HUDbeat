import time
from collections import deque
import numpy as np
import pandas as pd
import plotext as plx
import recordEEG as eeg

ymin = -1800
ymax = 1800
samples = 240

folder, filename = eeg.get_recent(raw = True)
#print(folder)
#print(file)

#for chunk in pd.read_csv(file, chunksize = samples):
#    print(chunk)

def getraw():
  #df = pd.read_csv(file, sep='\t')
  #row = df.tail(1)
  #row = df.iloc[-1]
  #raw = row.iloc[0].items

  #with filename.open('r') as f:
  #    last = deque(f,1)[0]
  #print(last)
  #print(row)
  with open(filename, 'r') as f:
      data = f.readlines()
      print(data[-1])
  #df = pd.read_csv(file, sep='\t', lineterminator='\n')
  #with open(file) as f:
  #    row = f.readlines()[-1]
      
      #row = f.tail(1)
  #row = df.tail(1)
  #return(df)    

#y = plx.sin()
#plx.scatter(y)
#plx.show()

while True:
  row = getraw()
  print(row)
  #print(df.tail)
  #print(df.iloc[-1][0])
  #print(df.iloc[-1].tolist())
  #print(data.tail(1))
  #print(data.iloc[-1:][1].items)
  #print(data.iloc[-1:])
  

  #eeg.get_raw(samples)

  plx.clear_color()
  plx.frame(False)
  plx.grid(False)
  plx.xaxes(False, False)
  plx.yaxes(False, False)
  #plx.xticks(None)
  #plx.yticks(None)

  #y=(data)
  #print(y)

  #yticks = [-ymax, -ymax/2, 0, ymax/2, ymax]
  #ylabels = [-ymax, int(-ymax/2), "0 µV ", int(ymax/2), ymax]
  #plx.yticks(yticks, ylabels)
  
  #plx.ylim(-ymax,ymax)
  #plx.scatter(y, marker = "dot", color='white')
  #plx.clear_terminal()
  #plx.show()

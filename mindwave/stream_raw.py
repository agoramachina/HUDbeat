import time
import numpy as np
import plotext as plx
import recordEEG as eeg

ymax = 1800
samples = 240

while True:

  data = eeg.get_raw(samples)

  plx.clear_plot()
  plx.colorless()
  plx.frame(False)
  plx.grid(False)
  plx.xaxis(False)
  plx.yaxis(False)
  plx.xticks(None)
  plx.yticks(None)

  y=(data)

  #yticks = [-ymax, -ymax/2, 0, ymax/2, ymax]
  #ylabels = [-ymax, int(-ymax/2), "0 µV ", int(ymax/2), ymax]
  #plx.yticks(yticks, ylabels)
  
  plx.ylim(-ymax,ymax)
  plx.scatter(y, marker = "dot", color='white')
  plx.clear_terminal()
  plx.show()

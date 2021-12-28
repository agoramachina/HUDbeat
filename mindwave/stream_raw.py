import time
import numpy as np
import plotext as plx
import recordEEG as eeg

while True:

  data = eeg.get_raw(samples = 240)
  plx.clear_plot()
  plx.clear_terminal()

  y=(data)
  ymax = 1800

  #plx.ticks(0,0)
  plx.xaxis(False)
  yticks = [-ymax, -ymax/2, 0, ymax/2, ymax]
  plx.xticks = []
  ylabels = [-ymax, int(-ymax/2), "0 µV ", int(ymax/2), ymax]

  #plx.xticks(None) 
  plx.yticks(yticks, ylabels)
  plx.ylim(-ymax,ymax)
  plx.scatter(y, marker = "dot")
  plx.colorless()
  plx.show()

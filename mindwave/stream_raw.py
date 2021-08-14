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

  plx.ticks(0,0)
  plx.xaxes(False)
  yticks = [-ymax, -ymax/2, 0, ymax/2, ymax]
  ylabels = [-ymax, int(-ymax/2), "0 µV ", int(ymax/2), ymax]
  
  plx.yticks(yticks, ylabels)
  plx.ylim(-ymax,ymax)
  plx.plot(y)
  plx.colorless()
  plx.show()

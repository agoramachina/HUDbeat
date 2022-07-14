import time
import numpy as np
import plotext as plx
import recordEEG as eeg

while True:

  data = eeg.get_raw(samples = 240)
  
  plx.clear_figure()
  plx.clear_terminal()
  plx.clear_color()

  y=(data)
  ymax = 1800
  
  plx.xaxes(False, False)
  plx.yaxes(True, False)
  yticks = [-ymax, -ymax/2, 0, ymax/2, ymax]
  ylabels = [-ymax, int(-ymax/2), "0 µV ", int(ymax/2), ymax]
 
  plx.xticks([])
  plx.yticks(yticks, ylabels)
  plx.ylim(-ymax,ymax)
  plx.plot(y)
  #plx.scatter(y)
  plx.show()

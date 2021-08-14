import time
import numpy as np
import plotext as plx
import recordEEG as eeg

while True:

  data = eeg.get_raw(samples = 240)
  plx.clear_plot()
  plx.clear_terminal()
  #print(plx.terminal_size())
  y=(data)

  ymax = 1600

  plx.ticks(0,0)
  plx.xaxes(False)
  plx.yticks([-1600,-800,0,800,1600])
  plx.ylim(-ymax,ymax)
  plx.plot(y)
  plx.colorless()
  plx.show()

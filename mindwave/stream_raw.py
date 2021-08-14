import time
import numpy as np
import plotext as plx
import recordEEG as eeg

while True:

  data = eeg.get_raw()
  plx.clear_plot()
  plx.clear_terminal()

  y=(data)

  plx.ticks(0,0)
  plx.xaxes(False)
  plx.yticks([-1600,-800,0,800,1600])
  plx.ylim(-1600,1600)
  plx.plot(y)
  plx.colorless()
  plx.show()

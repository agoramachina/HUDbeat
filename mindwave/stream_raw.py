import time
import numpy as np
import plotext.plot as plx
import recordEEG as eeg

while True:

  data = eeg.get_raw()
  plx.clear_plot()
  plx.clear_terminal()

  y=(data)

  plx.plot(y, line_color='white', axes=[False,False], rows=30, ticks=False)

  plx.show()

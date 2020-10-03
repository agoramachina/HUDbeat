import time
import numpy as np
import plotext.plot as plx
import recordEEG as eeg

while True:

  data = eeg.Datapoints(eeg.get_raw())
  plx.clear_plot()
  plx.clear_terminal()

  #x=(data.raw[0])
  y=(data)

  plx.plot(y, line_color='red')


  plx.show()
  time.sleep(1)

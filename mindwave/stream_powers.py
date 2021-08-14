import time
import numpy as np
import plotext as plx
import recordEEG as eeg

while True:

  data = eeg.Datapoints(eeg.get_samples(30))
  plx.clear_plot()
  plx.clear_terminal()

  y=np.log(data.powers)

  plx.plot(data.times,y[0]) #, line_color='red')
  plx.plot(data.times,y[1]) #, line_color='orange')
  plx.plot(data.times,y[2]) #, line_color='green')
  plx.plot(data.times,y[3]) #, line_color='green')
  plx.plot(data.times,y[4]) #, line_color='blue')
  plx.plot(data.times,y[5]) #, line_color='cyan')
  plx.plot(data.times,y[6]) #, line_color='violet')
  plx.plot(data.times,y[7]) #, line_color='violet')
  plx.colorless()

  plx.show()
  #time.sleep(1)

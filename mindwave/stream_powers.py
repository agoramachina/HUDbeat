import time
import numpy as np
import plotext as plx
import recordEEG as eeg

colors = ['red', 'gold', 'green', 'basil', 'indigo', 'blue', 'lilac', 'violet']

while True:

  data = eeg.Datapoints(eeg.get_samples(samples = 30))
  plx.clear_plot()
  plx.clear_terminal()

  plx.colorless()

  plx.yscale('log')

  plx.ticks(0,0)
  plx.xaxes(False)
  plx.yaxes(False)


  for i in range(8):
      plx.plot(data.times, data.powers[i], color=colors[i], marker = "•")
            
  plx.show()
  time.sleep(1)

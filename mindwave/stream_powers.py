import time
import numpy as np
import plotext as plx
import recordEEG as eeg

samples = 30
colors = ['red', 'gold', 'green', 'basil', 'indigo', 'blue', 'lilac', 'violet']

while True:

  data = eeg.Datapoints(eeg.get_samples(samples))
  plx.clear_plot()
  plx.clear_terminal()

  plx.colorless()

  plx.yscale('log')

  plx.ticks(0,0)
  plx.xaxes(False)
  #plx.yaxes(False)


  yt = []
  for i in range(8):
      plx.plot(data.times, data.powers[i], color=colors[i], marker = "•")
      yt.append(data.powers[i][0])
  yt.reverse()
  plx.yticks(yt)

      
  plx.show()
  time.sleep(1)

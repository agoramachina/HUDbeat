# although EEG band power units are typically represented by V²/Hz,
# the values reported by the mindwave have undergone transformations
# such that there is no longer a simple voltage correlation.
# reported values are meaningful relative to each other over time,
# but should not be considered to have formal units.
# 
# for more details, see:
# http://support.neurosky.com/kb/development-2/eeg-band-power-values-units-amplitudes-and-meaning

import time
import numpy as np
import plotext as plx
import recordEEG as eeg

<<<<<<< HEAD
colors = ['red','yellow',5,'green','blue',6,11,10]
=======
#colors = ['red', 'orange', 'green', 'basil', 'indigo', 'blue', 'lilac', 'violet']

colors = [197, 214, 154, 28, 45, 27, 165, 90]

>>>>>>> main

while True:

  try:
    data = eeg.Datapoints(eeg.get_samples())
    print(data)
  except(ValueError, IndexError):
    data = eeg.Datapoints(len(eeg.get_samples().times))
    
<<<<<<< HEAD
  plx.clear_color()
  plx.clear_terminal()

  #plx.colorless()
  #plx.canvas_color('black')
  plx.axes_color(16)
  #plx.ticks_color('black')
  

  plx.yscale('log')

  #plx.xticks(None)
  #plx.yticks(None)
  plx.xaxes(False)
  plx.yaxes(False)
=======
  plx.clear_figure()
  plx.clear_terminal()
  plx.canvas_color('black')  

  plx.yscale('log')
  plx.xticks([])
  plx.yticks([])
  plx.xaxes(False, False)
  plx.yaxes(False, False)
>>>>>>> main

  for pow in data.powers:
      #print(data.times)
      print()
      for i in range(8):
        print(pow[i])
  #for i in range(8):
  #    #print(data.powers[i])
  #    for pow in data.powers[i]:
  #       plx.plot(data.powers[i], color=colors[i], marker = "•")
           
  #plx.show()
  time.sleep(1)



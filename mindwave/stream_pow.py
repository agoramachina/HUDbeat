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

#colors = ['red', 'orange', 'green', 'basil', 'indigo', 'blue', 'lilac', 'violet']

colors = [197, 214, 112, 28, 45, 27, 165, 90]


while True:

  try:
    data = eeg.Datapoints(eeg.get_samples(samples = 30))
  except(ValueError, IndexError):
    data = eeg.Datapoints(eeg.get_samples())
    
  plx.clear_figure()
  plx.clear_terminal()
  plx.canvas_color('black')  

  plx.yscale('log')
  plx.xticks([])
  plx.yticks([])
  plx.xaxes(False, False)
  plx.yaxes(False, False)

  for i in range(8):
      plx.plot(data.times, data.powers[i], color=colors[i], marker = "•")
            
  plx.show()
  time.sleep(1)

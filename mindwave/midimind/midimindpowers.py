import time, glob, os, sys, io, math
from collections import deque
import numpy as np
import pandas as pd
import rtmidi_python as rtmidi
from rtmidi_python import MidiOut

# Find most recent file and folder
dir = max([f.path for f in os.scandir('/home/agoramachina/HUDbeat/mindwave/EEG_data/') if f.is_dir()])
file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

# get last n samples
def get_samples(samples=30):
    with open (file, 'r') as f:
        q = deque(f,samples+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        return dfq

# play notebuffer
def play_arp(midiout,notes):

    velocity = 80
    for note in notes:
      midiout.send_message([0x90, note, velocity])
      time.sleep(.5/len(notes))
      midiout.send_message([0x80, note, 0])

def play(midiout,pow):
    if (pow < 9):
        play_arp(midiout, [60])
    if (9 <= pow < 10):
        play_arp(midiout, [63])
    if (10 <= pow < 11):
        play_arp(midiout, [67])
    if (11 <= pow):
        play_arp(midiout, [72])
    if (pow > 11):
        play_arp(midiout, [60,72])


# main
def main():

    midiout = []
    
    for i in range(0,8):
        midiout.append(rtmidi.MidiOut(b'rtmidi pow'))
        midiout[i].open_port(i+1)

    while(True):
      try:
          samples = 30
          data = get_samples(samples)
          rows, cols = data.shape
          
                   
          signal = data.iloc[:,1]
          powers = data.iloc[:,4:12]

          mins = np.log(powers.min().values)
          maxs = np.log(powers.max().values)
          means = np.log(powers.mean().values)
          ranges = maxs - mins
          difs = np.log(powers.iloc[[0,-1]].values) - np.log(powers.iloc[[0,-2]].values)
                    
          #print(np.log(powers.values[0]).round(decimals=3))
          #print("%2.3f" %np.log(powers.values[0,0]))
          for pow in powers.values[0]:
              print("%2.3f" %np.log(pow), end='\t')
          print()
          
          #midiout[0].send_message([0x90,60,127])

          play(midiout[0],np.log(powers.values[0,0]))
                    
      except (KeyboardInterrupt):
          for midi in midiout:
              midi.send_message([120]) # all sound off
              del midi
          print("\n\nGoodbye!")
          sys.exit()

      for midi in midiout:
          midi.send_message([120]) # all sound off
          del midi
# init
if __name__ == '__main__':

    os.system('cls' if os.name == 'nt' else 'clear')

    #df = pd.read_csv(file,header=1)
    #header = list(df)

    main()



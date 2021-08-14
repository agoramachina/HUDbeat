import time, glob, os, sys, io, math
from collections import deque
import numpy as np
import pandas as pd
import rtmidi_python as rtmidi
from rtmidi_python import MidiOut
from music21 import *

# Find most recent file and folder
dir = max([f.path for f in os.scandir('/home/agoramachina/HUDbeat/mindwave/EEG_data/') if f.is_dir()])
file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

# get last n samples
def get_samples(samples=8):
    with open (file, 'r') as f:
        q = deque(f,samples+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfv = dfq.values
        return dfq


# main
def main():

    sp = midi.realtime.StreamPlayer(notes)
    
    
    mt = midi.MidiTrack(1)
    mel = midi.MidiEvent(mt)


    while(True):
      try:
          data = get_samples()
          signal = data.iloc[:,1]
          atn = data.iloc[:,2]
          med = data.iloc[:,3]
          powers = data.iloc[:,4:12]

          print(atn.values[0], med.values[0])
          print(powers.values[:])


      except (KeyboardInterrupt):
          #midiout.send_message([120]) # all sound off
          sys.exit()

    del midiout

# init
if __name__ == '__main__':

    os.system('cls' if os.name == 'nt' else 'clear')

    df = pd.read_csv(file,header=1)
    header = list(df)

    main()



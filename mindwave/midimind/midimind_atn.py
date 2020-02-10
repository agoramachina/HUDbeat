import time, glob, os, io, math
from collections import deque
import numpy as np
import pandas as pd
import rtmidi_python as rtmidi
from rtmidi_python import MidiOut

# Find most recent file and folder
dir = max([f.path for f in os.scandir('/home/agoramachina/HUDbeat/mindwave/EEG_data/') if f.is_dir()])
file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

# get last n samples
def get_samples(samples=1):
    with open (file, 'r') as f:
        q = deque(f,samples+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfv = dfq.values
        return dfq

# play notebuffer      
def play_notes(midiout,notes):

    velocity = 80
    for note in notes:
      midiout.send_message([0x90, note, velocity])
      time.sleep(.5/len(notes))
      midiout.send_message([0x80, note, 0])

def play(midiout,atn):
    if (0 <= atn < 20):
        play_notes(midiout, [60])
    if (20 <= atn < 40):
        play_notes(midiout, [60,63,67])
    if (40 <= atn < 60):
        play_notes(midiout, [60,63,67,63])
    if (60 <= atn < 80):
        play_notes(midiout, [60,63,67,72])
    if (atn > 80):
        play_notes(midiout, [60,63,67,72,67,63])

def notebuffer():
    tempo = 120
    velocity = 80
    root = 60		 # tonic

# main      
def main():

    midiout = rtmidi.MidiOut(b'rtmidi out')
    available_ports = midiout.ports

    if available_ports:
        midiout.open_port(0)
    else:
        midiout.open_virtual_port("rtmidi viritual midi")
       
  
    while (True):
        data = get_samples()
        signal = data.iloc[:,1]
        atn = data.iloc[:,2]
        med = data.iloc[:,3]
        powers = data.iloc[:,4:12]

        print(atn.values[0])
        play(midiout,atn.values[0])

    del midiout
    
# init
if __name__ == '__main__':

    os.system('cls' if os.name == 'nt' else 'clear')

    df = pd.read_csv(file,header=1)
    header = list(df)
    
    main()
    


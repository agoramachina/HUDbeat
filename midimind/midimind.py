import time, glob, os, io, math
from collections import deque
import numpy as np
import pandas as pd
import rtmidi
#from midioutwrapper import MidiOutWrapper

# Find most recent file and folder
dir = max([f.path for f in os.scandir('../mindwave-mobile/EEG_data/') if f.is_dir()])
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
def play_notes(notes):

    velocity = 100
    
    midiout = rtmidi.MidiOut()
    midiout.open_port(1)
    with midiout:
    	for note in notes:
       	  midiout.send_message([0x90, note, velocity])
          time.sleep(.5/len(notes))
          midiout.send_message([0x80, 60, 0])
    del midiout

def play_atn(atn):
    if (0 <= atn < 20):
        play_notes([60])
    if (20 <= atn < 40):
        play_notes([60,63,67])
    if (40 <= atn < 60):
        play_notes([60,63,67,63])
    if (60 <= atn < 80):
        play_notes([60,63,67,72])
    if (atn > 80):
        play_notes([60,63,67,72,67,63])

def play_med(med):
    if (0 <= med < 20):
        play_notes([60])
    if (20 <= med < 40):
        play_notes([60,63,67])
    if (40 <= med < 60):
        play_notes([60,63,67,63])
    if (60 <= med < 80):
        play_notes([60,63,67,72])
    if (med > 80):
        play_notes([60,63,67,72,67,63])

def notebuffer():
    tempo = 120
    velocity = 100
    root = 60
    scale = minor
    
    
# main      
def main():
    while (True):
    	os.system('cls' if os.name == 'nt' else 'clear')

    	data = get_samples()
    	signal = data.iloc[:,1]
    	atn = data.iloc[:,2]
    	med = data.iloc[:,3]
    	powers = data.iloc[:,4:12]

    	play_atn(atn.item())

    	#notes = [60,63,67]
    	#play_notes(notes)
# init
if __name__ == '__main__':

    df = pd.read_csv(file,header=1)
    header = list(df)

    main()


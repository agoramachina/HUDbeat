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
def notequeue(notes):

    velocity = 80
    for note in notes:
        midiout.send_message([0x90, note, velocity])
        time.sleep(.5/len(notes))
        midiout.send_message([0x80, note, 0])

def play_notes(med):
    if (0 <= med < 20):
        notequeue([60])
        notequeue([63])
        notequeue([67])
    #if (20 <= med < 40):
    #    notequeue([60,63,67])
    #if (40 <= med < 60):
    #    notequeue([60,63,67,63])
    #if (60 <= med < 80):
    #    notequeue([60,63,67,72])
    if (med > 20):
        velocity = 50
        midiout.send_message([0x90, 24, velocity])
        midiout.send_message([0x90, 48, velocity])
        time.sleep(1)
        midiout.send_message([0x80, 24, 0])
        midiout.send_message([0x80, 48, 0])
        

# main      
def main(midiout):

    with midiout:    
        while (True):    
    	    data = get_samples()
    	    signal = data.iloc[:,1]
    	    med = data.iloc[:,3]
    	    play_notes(med.item())

# init
if __name__ == '__main__':

    os.system('cls' if os.name == 'nt' else 'clear')

    df = pd.read_csv(file,header=1)
    header = list(df)

    midiout = rtmidi.MidiOut()
    midiout.open_virtual_port("midimind_med")
    main(midiout)


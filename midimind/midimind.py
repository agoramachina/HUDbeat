import time, glob, os, io, math
from collections import deque
import numpy as np
import pandas as pd
import rtmidi
#from midioutwrapper import MidiOutWrapper

# Find most recent folder and file
#def get_file():
#    dir = max([f.path for f in os.scandir('../mindwave-mobile/EEG_data/') if f.is_dir()])
#    file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)
#    return file

# get last n samples
def get_samples(samples=1):
    with open (file, 'r') as f:
        q = deque(f,samples+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfv = dfq.values
        return dfq
        

midiout = rtmidi.MidiOut()

#21-108
#60,72

#tempo = 
#def key(tonic, scale, octaves)

#bohlen-pierce
#def scale(tonic, interval)

#class scale():
#	def mode() # mode = scale+behavior
#	ionian
#	  interval = [2,2,1,2,2,2,1]
#	dorian
#	  interval = [2,1,2,2,2,1,2]
#	phrygian
#	  interval = [1,2,2,2,1,2,2]
#	lydian
#	  interval = [2,2,2,1,2,2,1]
#	mixolydian
#	  interval = [2,2,1,2,2,1,2]
#	aeolian
#	  interval = [2,1,2,2,1,2,2]
#	locrian
#	  interval = [1,2,2,1,2,2,2]
#
#	def scale
#	  chromatic (12)
#	  octatonic (8) #default
#	  heptatonic (7)
#	  hexatonic (6)
#	  pentatonic (5)
#	  tetratonic, tritonic, ditonic, monotonic
#
#	  interval: hemitonic, cohemitonic, etc
#	  symmetry: palindromic, chiral, rotational (messiaen)
#
#	def chord (tonic,mode, scale, increment)
#	
#	self.major = ionian
#	self.minor = aeolian
#	self.
#	circle-of-fifths = [1,2,2,1,2,2,2] #get identity matrix
#	
#def rescale(a,b,c,d):
    
def play_notes(notes):
    velocity = 100
    midiout.open_port(1)
    with midiout:
    	for note in notes:
       	  midiout.send_message([0x90, note, velocity])
          time.sleep(.5/len(notes))
          midiout.send_message([0x80, 60, 0])
      
def main():
    while (True):
        os.system('cls' if os.name == 'nt' else 'clear')

        samples = 1	#number of samples to get

        midiout = rtmidi.MidiOut()

        root = 60	#root key
	
        data = get_samples(eeg_file, samples)
        powers = data.iloc[:,4:12]
        print(powers)
    	time.sleep(1)


if __name__ = '__main__':   
    # Find most recent folder and file
    dir = max([f.path for f in os.scandir('../mindwave-mobile/EEG_data/') if f.is_dir()])
    file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)
 
    # Get initial data frame
    df = pd.read_csv(file,header=1)
    header = list(df)

    main()




with midiout:
    note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
    note_off = [0x80, 60, 0]

root = 60
#mode = minor

attn = 50



notes = [60,63,67,72,75,79,84]

if 0 <= attn < 10:
    notes = [60]
elif 10 <= attn < 20:
    notes = [60,63]
elif 20 <= attn < 30:
    notes = [60,63,67]
elif 30 <= attn < 40:
    notes = [60,63,67,63]
elif 40 <= attn < 50:
    notes = [60,63,67,72]
elif 50 <= attn < 60:
    notes = [60,63,67,72,67] 
elif 60 <= attn < 70:
    notes = [60,63,67,72,67,63]
elif 70 <= attn < 80:
    notes = [60,63,67,72,75,79]
elif 80 <= attn < 90:
    notes = [60,63,67,72,75,79,84]
elif 90 <= attn <= 100:
    notes = [60,63,67,72,75,79,84,79,75,72,67,63]    

play_notes(notes)

del midiout


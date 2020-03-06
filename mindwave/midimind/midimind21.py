import time, glob, os, io, math
from collections import deque
import numpy as np
import pandas as pd
from music21 import *

# Find most recent folder and file
def get_file():
  global file
  dir = max([f.path for f in os.scandir('../EEG_data/') if f.is_dir()])
  file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)
  return file

# get initial data frame
def make_dataframe():
  global df
  df = pd.read_csv(file,header=1)
  header = list(df)
  return df

# get last n samples
def get_samples(samples):
    with open (file, 'r') as f:
        q = deque(f,samples+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfv = dfq.values
        return dfq

def main():

   get_file()
   df = make_dataframe()

   mt = midi.MidiTrack(1)
   dt = midi.DeltaTime(mt)
   mel = midi.MidiEvent(mt)
   mel.type = midi.ChannelVoiceMessages.NOTE_ON
   mel.channel = 1
   mel.time = 60
   mel.pitch = 60
   mel.velocity = 120

   while (True):

      os.system('cls' if os.name == 'nt' else 'clear')

      samples = 1
      data = get_samples(samples)

      times  = data.iloc[:,0]
      signals= data.iloc[:,1]

      attns  = data.iloc[:,2]
      meds   = data.iloc[:,3]

      powers = data.iloc[:,4:12]
      #print(powers.tail(10))

      deltas = powers.values[:,0]
      thetas = powers.values[:,1]
      alphas = powers.values[:,2]
      Alphas = powers.values[:,3]
      betas  = powers.values[:,4]
      Betas  = powers.values[:,5]
      gammas = powers.values[:,6]
      Gammas = powers.values[:,7]

      logs = np.log(powers.values[0,:])
      mins = powers.min().values
      maxs = powers.max().values
      means = powers.mean().values
      ranges = (powers.max() - powers.min()).values
      diffs = np.log(powers.values[samples-2,:]) - np.log(powers.values[samples-1,:])
      pstats = [[logs], [mins], [maxs], [means], [ranges], [diffs]]

      c1 = chord.Chord('C#4 E4 G#4')
      notes = converter.parse("tinynotation: 3/4 g8# a4 g#8 a4")
      notes.show('midi')

if __name__ == '__main__':

  environment.set('midiPath', '/usr/bin/timidity')
  #environment.set('musicxml', '/usr/bin/musescore')
  main()

#c1 = chord.Chord('C#4 E4 G#4')
#print (c1.commonName)
#notes = converter.parse("tinynotation: 3/4 g8# a4 g#8 a4")
#c1.show('midi')

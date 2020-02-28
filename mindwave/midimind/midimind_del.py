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
def get_samples(samples=1):
    with open (file, 'r') as f:
        q = deque(f,samples+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfv = dfq.values
        return dfq

class MidiOutWrapper:
    def __init__(self, midi, ch=1):
        self.channel = ch
        self._midi = midi

    def channel_message(self, command, *data, ch=None):
        """Send a MIDI channel mode message."""
        command = (command & 0xf0) | ((ch if ch else self.channel) - 1 & 0xf)
        msg = [command] + [value & 0x7f for value in data]
        self._midi.send_message(msg)

    def note_off(self, note, velocity=0, ch=None):
      """Send a 'Note Off' message."""
      self.channel_message(NOTE_OFF, note, velocity, ch=ch)

    def note_on(self, note, velocity=127, ch=None):
      """Send a 'Note On' message."""
      self.channel_message(NOTE_ON, note, velocity, ch=ch)

    def program_change(self, program, ch=None):
      """Send a 'Program Change' message."""
      self.channel_message(PROGRAM_CHANGE, program, ch=ch)

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


    midiout = rtmidi.MidiOut(b'rtmidi delta')
    midiout.open_port(1)

    while(True):
      try:
          data = get_samples()
          signal = data.iloc[:,1]
          powers = data.iloc[:,4:12]

          print("%2.3f" %np.log(powers.values[0,0]))
          play(midiout,np.log(powers.values[0,0]))
                   
      except (KeyboardInterrupt):
          midiout.send_message([120]) # all sound off
          del midiout
          sys.exit()

    del midiout

# init
if __name__ == '__main__':

    os.system('cls' if os.name == 'nt' else 'clear')

    df = pd.read_csv(file,header=1)
    header = list(df)

    main()



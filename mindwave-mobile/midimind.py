import time
import rtmidi

midiout = rtmidi.MidiOut()
midiout.open_port(1)

#21-108
#60,72

#def key(tonic, scale, octaves)

#bohlen-pierce
#def scale(tonic, interval)

with midiout:
    note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
    note_off = [0x80, 60, 0]
    midiout.send_message(note_on)
    time.sleep(0.5)
    midiout.send_message(note_off)
    time.sleep(0.1)

del midiout

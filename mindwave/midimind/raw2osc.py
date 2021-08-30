import time, glob, os, csv
import numpy as np

from pythonosc import udp_client
from pythonosc import osc_message_builder
from pythonosc import osc_bundle_builder

# OS friendly formatting
os.system('cls' if os.name == 'nt' else 'clear')

# find most recent folder and file
dir = max([f.path for f in os.scandir('./EEG_data/') if f.is_dir()])
file = max(glob.glob(os.path.join(dir, 'EEGlogRAW_*.csv')),key=os.path.getctime)

# define ip and port
#ip = '127.0.0.1' # sonic-pi
#port 57121	 # sonic-pi
#ip = '192.168.1.248'	# supercollider
#port = 4560		# supercollider
ip = '192.168.1.100'	# external
port = 57120

# setup OSC server
sender = udp_client.SimpleUDPClient(ip, port)

while True:

  # Get data
  data = np.genfromtxt(file, dtype=float, delimiter='\t', names=True)
    
  #line = data[-1]
  #print (line[1])

  # Build and send OSC message
  #msg = osc_message_builder.OscMessageBuilder(address = "/eeg/raw")
  #msg.add_arg(line[1], arg_type='i')
  #for value in line:   
  #    msg.add_arg(value, arg_type='i')
  #msg = msg.build()
  #sender.send(msg)
  #time.sleep(1)



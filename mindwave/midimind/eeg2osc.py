import time, glob, os, csv
import numpy as np

from pythonosc import udp_client
from pythonosc import osc_message_builder

# OS friendly formatting
os.system('cls' if os.name == 'nt' else 'clear')

# fond most recent folder and file
dir = max([f.path for f in os.scandir('./EEG_data/') if f.is_dir()])
file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

# define ip and port
#ip = '127.0.0.1' # sonic-pi
#port 57121	 # sonic-pi
#ip = '192.168.1.248'	# supercollider
#port = 4560		# supercollider
ip = '192.168.1.26'	# external
port = 57120

# setup OSC server
sender = udp_client.SimpleUDPClient(ip, port)


while True:

  # Get data
  data = np.genfromtxt(file, dtype=float, delimiter=',', names=True)
    
  line = data[-1]
  for i in range(4, 12):
    line[i] = np.round(np.log(line[i]), decimals = 3)
  print (line)

  # Build and send OSC message
  msg = osc_message_builder.OscMessageBuilder(address = "/eeg")
  for value in line:
      msg.add_arg(value, arg_type='f')
  msg = msg.build()
  sender.send(msg)
  time.sleep(1)

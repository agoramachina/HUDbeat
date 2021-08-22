import time, glob, os, csv
import numpy as np

from pythonosc import udp_client
from pythonosc import osc_message_builder

# OS friendly formatting
os.system('cls' if os.name == 'nt' else 'clear')

# fond most recent folder and file
dir = max([f.path for f in os.scandir('../EEG_data/') if f.is_dir()])
file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

# define ip and port
#ip = '127.0.0.1'
ip = '192.168.1.100'
port = 4560

# setup OSC server
sender = udp_client.SimpleUDPClient(ip, port)


while True:

  # Get data
  data = np.genfromtxt(file, dtype=float, delimiter=',', names=True)
  line = data[-1]
  for i in range(4, 12):
    line[i] = np.log(line[i])
  print (line)

  # Build and send OSC message
  msg = osc_message_builder.OscMessageBuilder(address = "/eeg")
  for value in line:
      msg.add_arg(value, arg_type='f')
  msg = msg.build()
  sender.send(msg)
  time.sleep(1)

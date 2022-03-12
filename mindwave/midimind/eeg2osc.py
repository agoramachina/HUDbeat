import time, glob, os, csv
import numpy as np

from pythonosc import udp_client
from pythonosc import osc_message_builder
from pythonosc import osc_bundle_builder

# OS friendly formatting
os.system('cls' if os.name == 'nt' else 'clear')

# find most recent folder and file
dir = max([f.path for f in os.scandir('../EEG_data/') if f.is_dir()])
file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

# define ip and port
#port =  57120		# sc
#ip = '192.168.1.26'	# sc
ip = '192.168.1.88'
port = 57120	#sp

# setup OSC server
sender = udp_client.SimpleUDPClient(ip, port)

while True:

# Get data
  data = np.genfromtxt(file, dtype=float, delimiter=',', names=True)
  #print(data[-1])

  line = data[-1]
  for i in range(4, 12):
    line[i] = np.log(line[i]) #np.round(np.log(line[i]))
  print (line)

  
    
  # Build and send OSC message
  msg = osc_message_builder.OscMessageBuilder(address = 'eeg')
  for value in line:   
      msg.add_arg(value, arg_type='f')
  msg = msg.build()
  sender.send(msg)
  time.sleep(1)




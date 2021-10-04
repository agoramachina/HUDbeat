import time, glob, os, csv
import numpy as np

from pythonosc import udp_client
from pythonosc import osc_message_builder
from pythonosc import osc_bundle_builder

# OS friendly formatting
os.system('cls' if os.name == 'nt' else 'clear')

# find most recent folder and file
dir = max([f.path for f in os.scandir('./EEG_data/') if f.is_dir()])
file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

# define ip and port
#ip = '127.0.0.1'
##port 57121		# sonic-pi
##port = 4560		# supercollider
ip = '192.168.1.26'	# external
#ip = '192.168.56.1'
port = 4560

# setup OSC server
sender = udp_client.SimpleUDPClient(ip, port)

labels = ["time", "signal", "atn", "med", "delta", "theta", "l_alpha", "h_alpha", "l_beta", "h_beta", "l_gamma", "m_gamma"]

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

#  bundle = osc_bundle_builder.OscBundleBuilder(
#    osc_bundle_builder.IMMEDIATELY)
#  msg = osc_message_builder.OscMessageBuilder(address="/EEG/atnmed")
#  msg.add_arg(int(line[2]))
#  msg.add_arg(int(line[3]))
#  bundle.add_content(msg.build())

#  for i in range (4,12):
#    msg = osc_message_builder.OscMessageBuilder(address="/EEG/" + labels[i])
#    msg.add_arg(line[i])  
#    bundle.add_content(msg.build())
  
#  bundle = bundle.build()
#  sender.send(bundle)
#  time.sleep(1)
  

import time, datetime, glob, os, sys, io
from optparse import OptionParser
from collections import deque
import numpy as np

from pythonosc import udp_client
from pythonosc import osc_message_builder

# OS friendly formatting
os.system('cls' if os.name == 'nt' else 'clear')

# fond most recent folder and file
dir = max([f.path for f in os.scandir('../EEG_data/') if f.is_dir()])
file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

SLEEP_INTERVAL = 1.0

ip = '127.0.0.1'
port = 57121


sender = udp_client.SimpleUDPClient(ip, port)
#while True:
#    sender.send_message('/pow', [70, 100, 8, 100])


data = np.genfromtxt(file, dtype=int, delimiter=',', names=True)
print(data)
 
def tail(f):
    while True:
      where = f.tell()
      line = f.readline()
      if not line:
          time.sleep(SLEEP_INTERVAL)
          f.seek(where)
      else:
          yield (line)

def read_tail():
    with open (file, 'r') as f:
      for line in tail(f):
          line = line.strip()
          values = [i for i in line.split(',')]
          array = np.array(values)

          powers = array[4:len(array)]
          for pow in powers:
            pow = float(pow)
          print (powers)

          #for i in range (4, len(array)):
          #    array[i] = np.log(i)
          #    powers = array[i]
        
          #print(array)

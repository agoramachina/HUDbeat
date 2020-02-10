import time, datetime, glob, os, io, math
from collections import deque
import numpy as np
import pandas as pd
import curses
import gnuplotlib
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import style
#matplotlib.use('dumb')
import sparklines

samples = 60

class colors():
      reset = '\u001b[0m'
      delta = '\u001b[31m'
      theta = '\u001b[33m'
      lowAlpha = '\u001b[32m'
      highAlpha = '\u001b[32;1m'
      lowBeta = '\u001b[36m'
      highBeta = '\u001b[36;1m'
      lowGamma = '\u001b[35m'
      midGamma = '\u001b[35;1m'

class datapoints():
    def __init__(self, data):
    
      self.times = data.iloc[:,0]
      self.signals = data.iloc[:,1]
      
      self.attns = data.iloc[:,2]
      self.meds = data.iloc[:,3]

      self.powers = data.iloc[:,4:12]

      self.deltas = self.powers.values[:,0]
      self.thetas = self.powers.values[:,1]
      self.l_alphas = self.powers.values[:,2]
      self.h_alphas = self.powers.values[:,3]
      self.l_betas = self.powers.values[:,4]
      self.h_betas = self.powers.values[:,5]
      self.l_gammas = self.powers.values[:,6]
      self.m_gammas = self.powers.values[:,7]

      self.logs = np.log(self.powers.values[0,:])
      self.mins = self.powers.min().values
      self.maxs = self.powers.max().values
      self.means = self.powers.mean().values
      self.ranges = (self.powers.max() - self.powers.min()).values
      self.diffs = np.log(self.powers.values[samples-2,:]) - np.log(self.powers.values[samples-1,:])
            
# get last n samples
def get_samples(samples):
    with open (file, 'r') as f:
        q = deque(f,samples+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfv = dfq.values
        return dfq


def print_data(data):
    
#      print("t: " + time.strftime('%H:%M:%S', time.gmtime(data.times[samples-1])))
#      print("Signal: " + str(data.signals[samples-1]))

#      print()
#      print("attention: " + str(data.attns[samples-1]))
#      print("Meditation: " + str(data.meds[samples-1]))

      print("")
      print("      ╒══════════════════════════════════════════════════════════════════╕")
      print("      │  delta\t  theta\t  alpha\t  Alpha\t   beta\t   Beta\t  gamma\t  Gamma  │")
# δ θ α Α β Β γ Γ
      print("       ──────────────────────────────────────────────────────────────────┤", end = '')

      print("\n│ log │\t ", end = '')
      for log in data.logs: print("%6.3f" %(log), end = '\t ')

      print("│\n│ min │\t ", end = '')
      for min in data.mins: print("%6.3f" %np.log(min), end = '\t ')

      print("│\n│ max │\t ", end= '')
      for max in data.maxs: print("%6.3f" %np.log(max), end = '\t ')

      print("│\n│ avg │\t ", end = '')
      for mean in data.means: print("%6.3f" %np.log(mean), end = '\t ')

      print("│\n│ rng │\t ", end = '')
      for range in data.ranges: print("%6.3f" %np.log(range), end = '\t ')
      # range/max

      print("│\n│ dif │", end = '')
      for dif in data.diffs: print('\t %6.3f' %dif, end = '')

      print("  │\n┕━━━━━┙", end = '')
      print("──────────────────────────────────────────────────────────────────┘")

      time.sleep(1)
      os.system('cls' if os.name == 'nt' else 'clear')

def main():
   os.system('cls' if os.name == 'nt' else 'clear')

   while (True):
     try:
        data = datapoints(get_samples(samples))
        print_data(data)

     except ValueError:
        print("Please wait for data population...")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


      #stats = pd.DataFrame({[logs],[mins],[maxs],[means],[ranges],[diffs]},
      #	columns=['delta', 'theta', 'alpha', 'Alpha', 'beta', 'Beta', 'gamma', 'Gamma'],
      #	index=['log', 'min', 'max', 'mean','range', 'diff'])


if __name__ == '__main__':
  # Find most recent folder and file
  dir = max([f.path for f in os.scandir('./EEG_data/') if f.is_dir()])
  file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

  # get initial data frame
  df = pd.read_csv(file,header=1)
  header = list(df)

  main()

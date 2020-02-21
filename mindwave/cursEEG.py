import time, datetime, glob, os, sys, io, math
from collections import deque
import numpy as np
import pandas as pd
import curses
from curses import wrapper
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
      self.pow = [self.deltas, self.thetas, self.l_alphas, self.h_alphas, self.l_betas, self.h_betas, self.l_gammas, self.m_gammas]

      self.logs = np.log(self.powers.values[0,:])
      self.mins = np.log(self.powers.min().values)
      self.maxs = np.log(self.powers.max().values)
      self.means = np.log(self.powers.mean().values)
      self.ranges = self.maxs - self.mins
      self.diffs = np.log(self.powers.values[samples-2,:]) - np.log(self.powers.values[samples-1,:])
      self.stats = [self.logs, self.mins, self.maxs, self.means, self.ranges, self.diffs]
#np.log(min).round(decimals=3))
class wincurses:
    def __init__(self):
        self.time = curses.newwin(1, 20, 0, 0)
        self.time.addstr(0,0,"t: ")
        self.signal = curses.newwin(1,20,1,0)
        self.signal.addstr(0,0,"Signal: ")

        self.attn = curses.newwin(14,20,4,0)
        self.attn.addstr(0,2, "Attention: ")
        self.med = curses.newwin(14,20,5,0)
        self.med.addstr(0,2, "Meditation: ")

        self.powers = curses.newwin(10,26,7,0)
        self.powers.addstr(1,2,"Delta: ")
        self.powers.addstr(2,2,"theta: ")
        self.powers.addstr(3,2,"Low Alpha: ") 
        self.powers.addstr(4,2,"High Alpha: ")
        self.powers.addstr(5,2,"Low Beta: ")
        self.powers.addstr(6,2,"High Beta: ")
        self.powers.addstr(7,2,"Low Gamma: ")
        self.powers.addstr(8,2,"Mid Gamma: ")
        self.powers.box()

        self.stats_label = curses.newwin(11, 76, 7, 32)
        self.stats_label.addstr(0,6, "┌───────────────────────────────────────────────────────────────────┐")
        self.stats_label.addstr(1,6, "│   delta   theta   alpha   Alpha    beta    Beta   gamma   Gamma   │")
        self.stats_label.addstr(2,0, "┌─────")
        self.stats_label.addstr(3,0, "│ log ")
        self.stats_label.addstr(4,0, "│ min ")
        self.stats_label.addstr(5,0, "│ max ")
        self.stats_label.addstr(6,0, "│ avg ")
        self.stats_label.addstr(7,0, "│ rng ")
        self.stats_label.addstr(8,0, "│ dif ")
        self.stats_label.addstr(9,0, "└─────")
        #self.stats_label.box()

        self.stats = curses.newwin(8, 69, 9, 38)
        self.stats.box()
        
        self.windows = [self.time, self.signal, self.attn, self.med, self.powers, self.stats_label, self.stats]
        
# get last n samples
def get_samples(samples):
    with open (file, 'r') as f:
        q = deque(f,samples+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfv = dfq.values
        return dfq

def main():
   os.system('cls' if os.name == 'nt' else 'clear')
   
   stdscr = curses.initscr()
   curses.noecho()
   curses.cbreak()
   stdscr.keypad(True)
   #curses.start_color() ## removes bg opacity!

   #curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
   #curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

   win = wincurses()
   for w in win.windows:
       w.refresh()
   
   while (True):
     try:
        data = datapoints(get_samples(samples))
                
        win.time.addstr(0,4, str(time.strftime('%H:%M:%S', time.gmtime(data.times[samples-1]))))
        win.signal.addstr(0,8, str(data.signals[samples-1]) + "\t")
        
        win.attn.addstr(0,14, str(data.attns[samples-1]) + "\t")
        
        win.med.addstr(0,14,  str(data.meds[samples-1]) + "\t")

        #line=0
        #for pows in data.powers[samples-1]:
        #    for pow in pows:
        #        win.powers.addstr(line,12, str(pow) + "\t")
        #    line = line+1
                
        win.powers.addstr(1,16,str(data.deltas[samples-1]) + "\t")
        win.powers.addstr(2,16,str(data.thetas[samples-1]) + "\t")
        win.powers.addstr(3,16,str(data.l_alphas[samples-1]) + "\t")
        win.powers.addstr(4,16,str(data.h_alphas[samples-1]) + "\t")
        win.powers.addstr(5,16,str(data.l_betas[samples-1]) + "\t")
        win.powers.addstr(6,16,str(data.h_betas[samples-1]) + "\t")
        win.powers.addstr(7,16,str(data.l_gammas[samples-1]) + "\t")
        win.powers.addstr(8,16,str(data.m_gammas[samples-1]) + "\t")

        line = 1
        for stats in data.stats:
            s = " "
            for stat in stats:
                s = s + str("%6.3f" %stat.round(decimals=3) + "  ")
                win.stats.addstr(line,2,s)
            line = line+1

#        s = ""
#        for log in data.logs:
#            s = s + str(log.round(decimals=3)) + "\t" 
#        win.stats.addstr(1,6, s)

        for w in win.windows:
            w.refresh()

     except ValueError:
        #print("Please wait for data population...")
        time.sleep(1)
        #os.system('cls' if os.name == 'nt' else 'clear')
     except(KeyboardInterrupt):
         sys.exit()

if __name__ == '__main__':
  # Find most recent folder and file
  dir = max([f.path for f in os.scandir('./EEG_data/') if f.is_dir()])
  file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

  # get initial data frame
  df = pd.read_csv(file,header=1)
  header = list(df)

  main()

import time, datetime, glob, os, sys, io, math
from collections import deque
import numpy as np
import pandas as pd
from blessed import Terminal
import sparklines
from pyfiglet import Figlet

samples = 30

# OS friendly formatting
os.system('cls' if os.name == 'nt' else 'clear')

# find most recent folder and file
dir = max([f.path for f in os.scandir('./EEG_data/') if f.is_dir()])
file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

# get initial data frame
df = pd.read_csv(file,header=1)

# initialize blessed terminal
term = Terminal()



class Colors():
      reset = '\u001b[0m'
      delta = '\u001b[31m'
      theta = '\u001b[33m'
      lowAlpha = '\u001b[32m'
      highAlpha = '\u001b[32;1m'
      lowBeta = '\u001b[36m'
      highBeta = '\u001b[36;1m'
      lowGamma = '\u001b[35m'
      midGamma = '\u001b[35;1m'

class Datapoints():
    def __init__(self, data):

      self.times = data.iloc[:,0]
      self.signals = data.iloc[:,1]

      self.attns = data.iloc[:,2]
      self.meds = data.iloc[:,3]

      pows = self.Powers(data.iloc[:,4:12])
      self.powers = [pows.deltas, pows.thetas, pows.l_alphas, pows.h_alphas, pows.l_betas, pows.h_betas, pows.l_gammas, pows.m_gammas]

      stats = self.Stats(data.iloc[:,4:12])
      self.stats = [stats.logs, stats.mins, stats.maxs, stats.means, stats.ranges, stats.diffs]

    class Powers():
      def __init__(self,powers):
        self.deltas = powers.values[:,0]
        self.thetas = powers.values[:,1]
        self.l_alphas = powers.values[:,2]
        self.h_alphas = powers.values[:,3]
        self.l_betas = powers.values[:,4]
        self.h_betas = powers.values[:,5]
        self.l_gammas = powers.values[:,6]
        self.m_gammas = powers.values[:,7]

    class Stats():
      def __init__(self,powers):
        self.logs = np.log(powers.values[0,:])
        self.mins = np.log(powers.min().values)
        self.maxs = np.log(powers.max().values)
        self.means = np.log(powers.mean().values)
        self.ranges = self.maxs - self.mins
        self.diffs = np.log(powers.values[samples-2,:]) - np.log(powers.values[samples-1,:])


def printf(x, y, txt):
    f = Figlet(font='smblock')
    term.location(x,y)
    for line in f.renderText(txt).split("\n"):
        print(term.move_x(x) + line)
        
class wincurses:
    def __init__(self, stdscr):

        ymin,xmin = 0,0
        ymax,xmax = stdscr.getmaxyx()

        self.time = curses.newwin(5, 30, 0, xmax-23)
        self.signal = curses.newwin(5,xmax-24,0,1)

        self.attn = curses.newwin(14,20,5,0)
        self.attn.addstr(0,2, "Attention: ")
        self.med = curses.newwin(14,20,6,0)
        self.med.addstr(0,2, "Meditation: ")

        self.powers = curses.newwin(10,26,7,0)
        self.powers.addstr(1,1," Delta: \n  theta: \n  Low Alpha: \n  High Alpha: \n  Low Beta: \n  High Beta: \n  Low Gamma: \n  Mid Gamma: \n ")
        self.powers.box()

        self.stats_label = curses.newwin(11, 76, 7, 32)
        self.stats_label.addstr(0,6, "┌───────────────────────────────────────────────────────────────────┐")
        self.stats_label.addstr(1,6, "│   delta   theta   alpha   Alpha    beta    Beta   gamma   Gamma   │")
        self.stats_label.addstr(2,0, "┌─────\n│ log \n│ min \n│ max \n│ avg \n│ rng \n│ dif \n└─────  ")

        self.stats = curses.newwin(8, 69, 9, 38)
        self.stats.box()

        self.windows = [self.time, self.signal, self.attn, self.med, self.powers, self.stats_label, self.stats]


# get last n samples
def get_samples(samples):
    with open (file, 'r') as f:
        q = deque(f,samples+1)
        data = pd.read_csv(io.StringIO('\n'.join(q)))
        return data

def main():
   
   while (True):
     try:
        '''
        win = wincurses(stdscr)
        data = Datapoints(get_samples(samples))

        # Print Time & Signal
        printf(str(time.strftime('%H:%M:%S', time.gmtime(data.times[samples-1]))), win.time)
        printf(str(data.signals[samples-1]), win.signal)

        # Print Attn/Med
        win.attn.addstr(0,14, str(data.attns[samples-1]) + "\t")
        win.med.addstr(0,14,  str(data.meds[samples-1]) + "\t")

        # Print Powers
        line = 1
        for p in data.powers:
          win.powers.addstr(line,16,str(p[samples-1]) + "\t")
          line = line+1

        # Print Stats
        line = 1
        for stats in data.stats:
            s = " "
            for stat in stats:
                s = s + str("%6.3f" %stat.round(decimals=3) + "  ")
                win.stats.addstr(line,2,s)
            line = line+1

        # Refresh all windows (use noutrefresh and doupdate to prevent flickering)
        for w in win.windows:
            w.noutrefresh()
        curses.doupdate()
        '''

        data = Datapoints(get_samples(samples))
        
        print(term.home)
        # Print Time & Signal       
        printf(0,0, str(time.strftime('%H:%M:%S', time.gmtime(data.times[samples-1]))))
        printf(term.width-10,0, str(data.signals[samples-1]))

       

     # Error Handling (update this later to allow for lists < sample size)
     except(ValueError, IndexError):
        print(term.home + term.clear + "wait.")
        time.sleep(1)
        print(term.home + "wait..")
        time.sleep(1)
        print(term.home + "wait...")
        time.sleep(1)
     # Exit Program
     except(KeyboardInterrupt):
         sys.exit()

main()


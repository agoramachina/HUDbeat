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
        
# get last n samples
def get_samples(samples):
    with open (file, 'r') as f:
        q = deque(f,samples+1)
        data = pd.read_csv(io.StringIO('\n'.join(q)))
        return data

def main():
   
   while (True):
     try:

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


import time, glob, os, io, math
from collections import deque
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import style
#matplotlib.use('dumb')
import sparklines

samples = 60

# get last n samples
def get_samples(samples):
    with open (file, 'r') as f:
        q = deque(f,samples+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfv = dfq.values
        return dfq

#def get_stats():
#    stats = pd.DataFrame(LIST, index=['log', 'min', 'max', 'mean','range', 'diff'], columns = df.columns)

def main():
    
   while (True):

      os.system('cls' if os.name == 'nt' else 'clear')
 
      data = get_samples(samples)
      powers = data.iloc[:,4:12]
      print(powers.tail(10))

      deltas = powers.values[:,0]
      thetas = powers.values[:,1]
      alphas = powers.values[:,2]
      Alphas = powers.values[:,3]
      betas  = powers.values[:,4]
      Betas  = powers.values[:,5]
      gammas = powers.values[:,6]
      Gammas = powers.values[:,7]

      logs = np.log(powers.values[0,:])
      mins = powers.min().values
      maxs = powers.max().values
      means = np.log(powers.mean().values)
      ranges = (powers.max() - powers.min()).values
      diffs = powers.values[samples-2,:] - powers.values[samples-1,:]
      
      print("Power log", logs)
      print("Min: ", mins)
      print("Max: ", maxs)
      print("Mean: ", means)
      print("Range: ", ranges)
      print("Diff: ", diffs)
   
      ax.clear()
      #df.plot(kind='line',x=0,y=4, ax=ax)
      time.sleep(1)

if __name__ == '__main__':
  # Find most recent folder and file
  dir = max([f.path for f in os.scandir('./EEG_data/') if f.is_dir()])
  file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

  # get initial data frame
  df = pd.read_csv(file,header=1)
  header = list(df)

  samples = 60;

  # Initialize matplotlib graph
  fig = plt.figure()
  ax = fig.gca()

  main()
  #plt.show()
# get current axis from matplotlib


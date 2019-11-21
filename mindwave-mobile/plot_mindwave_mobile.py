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
      means = powers.mean().values
      ranges = (powers.max() - powers.min()).values
      diffs = np.log(powers.values[samples-2,:]) - np.log(powers.values[samples-1,:])
      pstats = [[logs], [mins], [maxs], [means], [ranges], [diffs]]
     
      #stats = pd.DataFrame({[logs],[mins],[maxs],[means],[ranges],[diffs]},
      #	columns=['delta', 'theta', 'lAlpha', 'hAlpha', 'lBeta', 'hBeta', 'lGamma', 'mGamma'],
      #	index=['log', 'min', 'max', 'mean','range', 'diff'])

      print("\nlog\t ", end = '')      
      for log in logs: print("%.3f" %(log), end = '\t ')
          
      print("\nmin\t ", end = '')
      for min in mins: print("%.3f" %np.log(min), end = '\t ')

      print("\nmax\t ", end= '')
      for max in maxs: print("%.3f" %np.log(max), end = '\t ')
 
      print("\navg\t ", end = '')
      for mean in means: print("%.3f" %np.log(mean), end = '\t ')
      
      print("\nrng\t ", end = '')
      for range in ranges: print("%.3f" %np.log(range), end = '\t ')

      print("\ndif", end = '')
      for dif in diffs:
          if dif >= 0: print('\t %.3f' %dif, end = '')
          if dif <  0: print('\t%.3f' %dif, end = '')
      print()
   
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


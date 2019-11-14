import time, glob, os, io, math
from collections import deque
import numpy as np
import pandas as pd
import mido
from mido import MidiFile

# Get last n samples of csv file
def get_samples(sample_size):
    with open (file, 'r') as f:
        q = deque(f,sample_size+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfv = dfq.values
        return dfq

def main():

  # get last n samples
  while (True):

      os.system('cls' if os.name == 'nt' else 'clear')

      samples = 10
      data = get_samples(samples)
      powers = data.iloc[:,4:12]
      print(powers)
      
      deltas = powers.values[:,0]
      thetas = powers.values[:,1]
      alphas = powers.values[:,2]
      Alphas = powers.values[:,3]
      betas  = powers.values[:,4]
      Betas  = powers.values[:,5]
      gammas = powers.values[:,6]
      Gammas = powers.values[:,7]

      #print("Deltas: ", deltas)

      power_log = np.log(powers.values[0,:])
      print("log: ", power_log.round(3))


      #print("PowerStats:")
      #power_stats = pd.DataFrame(list(powers))
      #print(power_stats)


      #print(str(powers.values[:,0].min()) + " / " + str(powers.values[:,0].max()))
      print("min: ", powers.min().values)
      print("max: ", powers.max().values)
      print("mean: ", powers.mean().values)
      print("diff: ", np.subtract(np.log(powers.values[samples-1,:]).round(3), np.log(powers.values[samples-2,:]).round(3)))

      time.sleep(1)

if __name__ == '__main__':
  # Find most recent folder and file
  dir = max([f.path for f in os.scandir('./EEG_data/') if f.is_dir()])
  file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

  # get initial data frame
  df = pd.read_csv(file,header=1)
  header = list(df)

  sample_size = 10;

  main()
  

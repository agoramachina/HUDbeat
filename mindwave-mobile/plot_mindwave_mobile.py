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

# Find most recent folder and file
dir = max([f.path for f in os.scandir('./EEG_data/') if f.is_dir()])
file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

# get initial data frame
df = pd.read_csv(file,header=1)
header = list(df)

sample_size = 10;
    
# Initialize matplotlib graph
fig = plt.figure()
ax = fig.add_subplot(1,sample_size,1)
#plt.show()

def get_samples(sample_size):
    with open (file, 'r') as f:
        q = deque(f,sample_size+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfv = dfq.values

# get last n samples
while (True):
    with open (file, 'r') as f:
        q = deque(f,sample_size+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfv = dfq.values

    os.system('cls' if os.name == 'nt' else 'clear')
    #print(dfq)

    powers = dfq.iloc[:,4:12]
    print(powers)
    #print(powers.values)

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
    print("Power log:")
    print(power_log)
    
    
    #print("Power Mean:")
    #print(powers.mean().values)

    #print("PowerStats:")
    #power_stats = pd.DataFrame(list(powers))
    #print(power_stats)
    

    #print(str(powers.values[:,0].min()) + " / " + str(powers.values[:,0].max()))
    print(powers.min().values)
    print(powers.max().values)
    print(powers.mean().values)

    #print("Power Max:")
    #print(powers.max())

    ax.clear()
    #df.plot(kind='line',x=0,y=4, ax=ax)
    time.sleep(1)
    

# get current axis from matplotlib
ax = plt.gca()

# plot power series
data.plot(kind='line',x=0,y=4,ax=ax)
data.plot(kind='line',x=0,y=5,ax=ax)
plt.show()


print(q)

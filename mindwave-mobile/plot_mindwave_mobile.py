import time
import glob
import os
import io
import math
from collections import deque
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import sparklines

# Find most recent folder and file
path = max(glob.glob(os.path.join('./EEG_data', '*/')))
paths = [os.path.join(path, file) for file in os.listdir(path)]
file = max(paths, key=os.path.getctime)

# get initial data frame
df = pd.read_csv(file,header=1)
header = list(df)

# Initialize matplotlib graph
fig = plt.figure()
ax = plt.gca()

sample_size = 10;
# get last n samples
while (True):
    with open (file, 'r') as f:
        q = deque(f,sample_size+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfn = dfq.values

    os.system('cls' if os.name == 'nt' else 'clear')
    print(dfq)

    powers = dfq.iloc[:,4:11]
    
    print("Power Mean:")
    print(powers.mean())
    print(powers)

    print("Power MinMax")
    print(powers.min())
    print(powers.max())
    
    #print("Power Max:")
    #print(powers.max())

    ax.clear()
    df.plot(kind='line',x=0,y=4, ax=ax)
    time.sleep(1)
    

# get current axis from matplotlib
ax = plt.gca()

# plot power series
data.plot(kind='line',x=0,y=4,ax=ax)
data.plot(kind='line',x=0,y=5,ax=ax)


print(q)

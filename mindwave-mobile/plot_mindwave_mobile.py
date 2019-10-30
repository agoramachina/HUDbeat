import time
import glob
import os
import io
from collections import deque
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Find most recent folder and file
path = max(glob.glob(os.path.join('./EEG_data', '*/')))
paths = [os.path.join(path, file) for file in os.listdir(path)]
file = max(paths, key=os.path.getctime)

# get initial data frame
df = pd.read_csv(file,header=1)
header = list(df)

# get last n samples
while (True):
    with open (file, 'r') as f:
        q = deque(f,10)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns

    os.system('cls' if os.name == 'nt' else 'clear')
    print(dfq)
    
    time.sleep(1)

# get current axis from matplotlib
ax = plt.gca()

# plot power series
data.plot(kind='line',x=0,y=4,ax=ax)
data.plot(kind='line',x=0,y=5,ax=ax)


print(q)

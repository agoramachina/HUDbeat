#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) 2019 agoramachina

# general dependencies
import time, datetime, os, sys, io, re, glob, math, csv, textwrap, bluetooth
from collections import deque

import numpy as np
import pandas as pd

from sparklines import sparklines

#Neurosky dependenies
from mindwavemobile.MindwaveDataPoints import *
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader

# define folder and file names
## default folder name is:      /home/$user/data/EEG_data/yyyy-mm-dd
## defualt file name is:        EEGlog_hh:mm:ss_ yyyy-mm-dd.csv
foldername = "./EEG_data/" + time.strftime("%Y-%m-%d/")
timestamp = time.strftime("%H-%M-%S")
filename = foldername + "EEGlog_" + timestamp + ".csv" #time.strftime("%H-%M-%S") + ".csv"
filename_raw = foldername + "EEGlogRAW_" + timestamp + ".csv" #+ time.strftime("%H-%M-%S") + ".csv"

samples = 30

class Colors:
    delta = '\u001b[31m'
    theta = '\u001b[33m'
    lowAlpha = '\u001b[32m'
    highAlpha = '\u001b[32;1m'
    lowBeta = '\u001b[36m'
    highBeta = '\u001b[36;1m'
    lowGamma = '\u001b[35m'
    midGamma = '\u001b[35;1m'
    reset = '\u001b[0m'


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

        ## CHANGE THIS! samples out of range
        self.diffs =  np.log(powers.values[-1,:]) - np.log(powers.values[samples-2,:])


# find most recent folder and file
def get_recent(raw = False):
    
    dir = foldername #max([f.path for f in os.scandir('./EEG_data/') if f.is_dir()])
    if (raw == True):
      file = max(glob.glob(os.path.join(dir, 'EEGlogRAW_*.csv')),key=os.path.getctime)
    else:
      file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)    
    return(dir, file)

# get last n samples
def get_samples(samples=30):

    # find most recent folder and file
    [dir,file] = get_recent()
    df = pd.read_csv(file,header=1)

    with open (file, 'r') as f:

        try: 
          q = deque(f,samples+1)
        except(ValueError):
          q = deque(f, len(df))

        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        return dfq

# get last n samples
def get_raw(samples=120):

    # find most recent folder and file
    [dir,file] = get_recent(raw=True) # Optimize this later!!!

    with open (file, 'r') as f:
        q = deque(f,samples+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)), delimiter='\t')
        return (dfq.iloc[:,1].values)


def open_writer():
    # initialize writer
  with open(filename, "a") as f:
      writer = csv.writer(f)
      #writer.writerow([current_datetime])
      writer.writerow(fields)
  with open(filename_raw, "a") as fr:
      writer = csv.writer(fr)
      writer.writerow([current_datetime])

def write_csv(data_row):
  with open(filename, "a") as f:
    writer = csv.writer(f)
    writer.writerow(data_row)

def write_raw(data_row):
  with open(filename_raw, "a") as f:
    writer = csv.writer(f)
    writer.writerow([data_row])

def pretty_print(data_row):
  os.system('cls' if os.name == 'nt' else 'clear')
  print("t: " + str(datetime.timedelta(seconds=float(data_row[0])))[:])
  print("Signal: " + data_row[1] + "\n")

  print("Attention: " + data_row[2])
  print("Meditation: " + data_row[3] + "\n")

  print("Delta: " + data_row[4])
  print("Theta: " + data_row[5])
  print("Low Alpha: " + data_row[6])
  print("High Alpha: " + data_row[7])
  print("Low Beta: " + data_row[8])
  print("High Beta: " + data_row[9])
  print("Low Gamma: " + data_row[10])
  print("Mid Gamma: " + data_row[11] + "\n")

def sparky(data_row, width, height):
  greek_head = ['δ', 'θ', 'α', 'Α', 'β', 'Β', 'γ', 'Γ']
  for line in sparklines(list(map(int,data_row[4:])), num_lines = height):
    line = ''.join(Colors.delta + width * str(line[0]) +
      Colors.theta + width * str(line[1]) +
      Colors.lowAlpha + width * str(line[2]) +
      Colors.highAlpha + width * str(line[3]) +
      Colors.lowBeta + width * str(line[4]) +
      Colors.highBeta + width * str(line[5]) +
      Colors.lowGamma + width * str(line[6]) +
      Colors.midGamma + width * str(line[7])+ Colors.reset)
    print(line)
  print(" " + "  ".join([g for g in greek_head]))


# MAIN FUNCTION
def main():

    data_row = []
    i = 0 #prevents opcode weirdness

    # open pipe
    #r, w = os.pipe()

    # continue writing as long as there exists data points to be read
    while(True):

        try:
          # get next data point
          dataPoint = mindwaveDataPointReader.readNextDataPoint()

          if (dataPoint.__class__ is RawDataPoint):
              rawData = str(dataPoint)[11:]
              #data_row=time.strftime("%H:%M:%S", time.localtime()), str(rawData)
              #write_raw(rawData)
              write_raw(str(round(time.time() - time_init, 5)) + "\t" + str(rawData))

          if (not dataPoint.__class__ is RawDataPoint):
              if (i==1):
                if (dataPoint.__class__ is PoorSignalLevelDataPoint):
                  data_row = []
                  data_row.append(int((time.time() - time_init)))
                data_cleaner = re.sub(r'[^\d\n]+', "", str(dataPoint))
                data_row.extend(data_cleaner.split())

          # special formatting for EEGPowers dataPoint
          if (dataPoint.__class__ is EEGPowersDataPoint):
              if (i==1):
                pretty_print(data_row)
                write_csv(data_row)
                sparky(data_row, 3, 5)
                #print()			#debug
                #for data in data_row:	#debug
                #  print(data, end=' ') 	#debug
                #print()			#debug
              i=1

        except(KeyboardInterrupt):
            sys.exit()


# __MAIN__
# initialize mindwave reader
if __name__ == '__main__':

  try:
    # initialize Mindwave
    print("Searching for Mindwave Mobile...")
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()

    if (mindwaveDataPointReader.isConnected()):


        # if the folder doesn't exist, create it
        if not os.path.exists(foldername):
            os.makedirs(foldername)

        # initialize csv rows and header
        current_datetime = datetime.datetime.now().__str__()
        time_init = time.time()
        data_row = []
        fields = ['Time', 'Signal', 'Attention', 'Meditation', 'Delta', 'Theta', 'Low Alpha', 'High Alpha', 'Low Beta', 'High Beta', 'Low Gamma', 'Mid Gamma']

        open_writer()
        #os.mkfifo("neurofifo")
        #fifo = open("neurofifo", 'a')

        # MAIN
        main()

    # ERROR: cannot connect to Mindwave Mobile
    else:
        print(textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " "))
  except(KeyboardInterrupt):
      print("\nExiting program.")

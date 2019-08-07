#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) 2019 agoramachina

# general dependencies
import bluetooth
import csv
import datetime
import getpass
import os
import re
import sys
import textwrap
import time

#import gnuplot #set term xterm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from termgraph import termgraph as tg
import lehar
import bashplotlib
import sparklines
# import data_hacks
import hipsterplot
#import termplot

#Neurosky dependenies
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPoints import EEGPowersDataPoint
from mindwavemobile.MindwaveDataPoints import PoorSignalLevelDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader

# define folder and file names
## default folder name is:      /home/$user/data/EEG_data/yyyy-mm-dd
## defualt file name is:        EEGlog_hh:mm:ss_ yyyy-mm-dd.csv
foldername = "/home/" + getpass.getuser() + "/data/EEG_data/" + time.strftime("%Y-%m-%d/")
filename = foldername + "EEGlog_" + time.strftime("%H:%M:%S_%Y-%m-%d") + ".csv"

# if the folder doesn't exist, create it
if not os.path.exists(foldername):
    os.makedirs(foldername)

def open_writer():
    # initialize writer
  with open(filename, "a") as f:
      writer = csv.writer(f)
      writer.writerow([current_datetime])
      writer.writerow(fields)

def write_csv(data_row):
  with open(filename, "a") as f:
      writer = csv.writer(f)
      writer.writerow(data_row)

def pretty_print(data_row):   
  os.system('cls' if os.name == 'nt' else 'clear')
  print("t: " + str(datetime.timedelta(seconds=float(data_row[0])))[:-3])
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

def plot_term(data_row):
  labels = [data_row[0]]
  data = [data_row[2], data_row[3]]
  normal_data = tg.normalize(int(data),2)
  len_categories = 2
  args = {'no_labels': True}
  colors = [91,92]
  tg.stacked_graph(labels, data, normal_data, len_categories, args, colors)

def animate(i):
    with open(filename,'r') as f:

      graph_data = f.readlines()[2:]
      lines = graph_data.split('\n')

      ts = []
      attns = []
      meds = []
      deltas = []
      thetas = []
      alpha_lows = []
      alpha_highs = []
      beta_lows = []
      beta_highs = []
      gamma_lows = []
      gamma_mids = []

      for line in lines[]:
          if len(line) > 1:
              t, signal, attn, med, delta, theta, alpha_low, alpha_high, beta_low, beta_high, gamma_low, gamma_mid = line.split(',')
              ts.append(float(x))
              signals.append(float(y))
      ax1.clear()
      ax1.plot(xs, ys)

# MAIN FUNCTION
def main():

    i = 0
    # continue writing as long as there exists data points to be read
    while(True):

      # get next data point
      dataPoint = mindwaveDataPointReader.readNextDataPoint()
      if (not dataPoint.__class__ is RawDataPoint):
          if (i is 1):
              if (dataPoint.__class__ is PoorSignalLevelDataPoint):
                  data_row = []
                  data_row.append("{0:.3f}".format(time.time() - time_init))
              data_cleaner = re.sub(r'[^\d\n]+', "", str(dataPoint))
              data_row.extend(data_cleaner.split())
      
      # special formatting for EEGPowers dataPoint        
      if (dataPoint.__class__ is EEGPowersDataPoint): 
          if (i is 1):        
              pretty_print(data_row)             
              #plot_term(data_row)
              write_csv(data_row)               
          i = 1


# __MAIN__
# initialize mindwave reader
if __name__ == '__main__':

    # initialize Mindwave
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    if (mindwaveDataPointReader.isConnected()): 

        # initialize csv rows and header
        current_datetime = datetime.datetime.now().__str__()
        time_init = time.time() 
        data_row = []
        fields = ['Time', 'Poor Signal Level', 'Attention', 'Meditation', 'Delta', 'Theta', 'Low Alpha', 'High Alpha', 'Low Beta', 'High Beta', 'Low Gamma', 'Mid Gamma']

        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)

        open_writer()

        # MAIN
        main()   
        
    # ERROR: cannot connect to Mindwave Mobile    
    else:
        print(textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " "))
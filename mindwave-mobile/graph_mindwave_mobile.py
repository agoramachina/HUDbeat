#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) 2019 agoramachina

# general dependencies
import bluetooth
import csv
import datetime
import os
import re
import sys
import textwrap
import time

#import gnuplot #set term xterm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import gnuplotlib as gp 
import numpy as np
# from collections import deque
#from termgraph import termgraph as tg
#import lehar
#import bashplotlib
from sparklines import sparklines
import pygal
from colors import *
#import data_hacks
#import hipsterplot
#import termplot

#Neurosky dependenies
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPoints import EEGPowersDataPoint
from mindwavemobile.MindwaveDataPoints import PoorSignalLevelDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader

# define folder and file names
## default folder name is:      /home/$user/data/EEG_data/yyyy-mm-dd
## defualt file name is:        EEGlog_hh:mm:ss_ yyyy-mm-dd.csv
foldername = "./EEG_data/" + time.strftime("%Y-%m-%d/")
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

def sparky(data_row, width, height):
  pretty_line = []
  for line in sparklines(list(map(int,data_row[4:])), num_lines = height):
    line = ''.join(color(str(line[0]), fg = '#FF0000') + 
      color(str(line[1]), fg = '#FFFF00') +
      color(str(line[2]), fg = '#00FF00') + 
      color(str(line[3]), fg = '#00AA00') +
      color(str(line[4]), fg = '#00FFFF') +
      color(str(line[5]), fg = '#0000FF') +
      color(str(line[6]), fg = '#FF00FF') + 
      color(str(line[7]), fg = '#AA00AA'))
    line = "".join([bar*width for bar in line])
    print(line)

def gal_plot(data_row):
  chart = pygal.Line(interpolate='cubic')
  chart.add('', list(map(int,data_row[4:])))
  print(chart.render_sparktext())

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
              write_csv(data_row)
              sparky(data_row, 3, 5)
              #gal_plot(data_row)
              
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

        open_writer()

        # MAIN
        main()   
        
    # ERROR: cannot connect to Mindwave Mobile    
    else:
        print(textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " "))
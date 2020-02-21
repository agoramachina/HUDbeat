#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) 2019 agoramachina

# general dependencies
import bluetooth, csv, datetime, os, re, sys, textwrap, time, math
from collections import deque

#import gnuplot #set term xterm
import matplotlib.pyplot as plt, matplotlib.animation as animation
from matplotlib import style
import gnuplotlib as gp
import numpy as np
import pandas as pd
# from collections import deque
from sparklines import sparklines

#Neurosky dependenies
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPoints import EEGPowersDataPoint
from mindwavemobile.MindwaveDataPoints import PoorSignalLevelDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader

# define folder and file names
## default folder name is:      /home/$user/data/EEG_data/yyyy-mm-dd
## defualt file name is:        EEGlog_hh:mm:ss_ yyyy-mm-dd.csv
foldername = "./EEG_data/" + time.strftime("%Y-%m-%d/")
filename = foldername + "EEGlog_" + time.strftime("%H-%M-%S") + ".csv"
filename_raw = foldername + "EEGlogRAW_" + time.strftime("%H-%M-%S") + ".csv"

# setup matplot animation
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# if the folder doesn't exist, create it
if not os.path.exists(foldername):
    os.makedirs(foldername)

class colors:

#    attn = '\033[95m'
#    med =
    delta = '\u001b[31m'
    theta = '\u001b[33m'
    lowAlpha = '\u001b[32m'
    highAlpha = '\u001b[32;1m'
    lowBeta = '\u001b[36m'
    highBeta = '\u001b[36;1m'
    lowGamma = '\u001b[35m'
    midGamma = '\u001b[35;1m'
#    rawData =
#    signalHi = green
#    signalMed = yellow
#    signalLow = red
    reset = '\u001b[0m'

def open_writer():
    # initialize writer
  with open(filename, "a") as f:
      writer = csv.writer(f)
      writer.writerow([current_datetime])
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
    line = ''.join(colors.delta + width * str(line[0]) +
      colors.theta + width * str(line[1]) +
      colors.lowAlpha + width * str(line[2]) +
      colors.highAlpha + width * str(line[3]) +
      colors.lowBeta + width * str(line[4]) +
      colors.highBeta + width * str(line[5]) +
      colors.lowGamma + width * str(line[6]) +
      colors.midGamma + width * str(line[7])+ colors.reset)
    print(line)
  print(" " + "  ".join([g for g in greek_head]))


# MAIN FUNCTION
def main():

    i = 0

    # continue writing as long as there exists data points to be read
    while(True):

        try:
          # get next data point
          dataPoint = mindwaveDataPointReader.readNextDataPoint()

          if (dataPoint.__class__ is RawDataPoint):
              rawData = str(dataPoint)[11:]
              #data_row=time.strftime("%H:%M:%S", time.localtime()), str(rawData)
              #print (rawData)
              write_raw(rawData)

          if (not dataPoint.__class__ is RawDataPoint):
              if (i == 1):
                  if (dataPoint.__class__ is PoorSignalLevelDataPoint):
                      data_row = []
                      data_row.append(int((time.time() - time_init)))
                  data_cleaner = re.sub(r'[^\d\n]+', "", str(dataPoint))
                  data_row.extend(data_cleaner.split())

          # special formatting for EEGPowers dataPoint
          if (dataPoint.__class__ is EEGPowersDataPoint):
              if (i == 1):
                  pretty_print(data_row)
                  write_csv(data_row)
                  sparky(data_row, 3, 5)
              i = 1

        except(KeyboardInterrupt):
            sys.exit()


# __MAIN__
# initialize mindwave reader
if __name__ == '__main__':

    # initialize Mindwave
    print("Searching for Mindwave Mobile...")
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()

    if (mindwaveDataPointReader.isConnected()):

        # initialize csv rows and header
        current_datetime = datetime.datetime.now().__str__()
        time_init = time.time()
        data_row = []
        fields = ['Time', 'Signal', 'Attention', 'Meditation', 'Delta', 'Theta', 'Low Alpha', 'High Alpha', 'Low Beta', 'High Beta', 'Low Gamma', 'Mid Gamma']

        open_writer()

        # MAIN
        main()

    # ERROR: cannot connect to Mindwave Mobile
    else:
        print(textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " "))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) 2019 agoramachina

# general dependencies
import bluetooth, csv, datetime, os, re, sys, textwrap, time, math
from collections import deque

#Neurosky dependenies
from mindwavemobile.MindwaveDataPoints import *
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader




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

class recordEEG:

    def __init__(self):

    # define folder and file names
    ## default folder name is:      /home/$user/data/EEG_data/yyyy-mm-dd
    ## defualt file name is:        EEGlog_hh:mm:ss_ yyyy-mm-dd.csv
       self.foldername = "./EEG_data/" + time.strftime("%Y-%m-%d/")
       self.filename = foldername + "EEGlog_" + time.strftime("%H-%M-%S") + ".csv"
       self.filename_raw = foldername + "EEGlogRAW_" + time.strftime("%H-%M-%S") + ".csv"

    def initializeEEG():
      # if the folder doesn't exist, create it
      if not os.path.exists(foldername):
        os.makedirs(foldername)

    def open_fifo():
        with open("neurofifo", 'w') as fifo:
            print("test")
        #fifo_read = open("neurofifo", 'r', 0) ## '0' removes buffering

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



# MAIN FUNCTION
def main():

    data_row = []
    i = 0 #prevents opcode weirdness

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

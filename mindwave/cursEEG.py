
# -*- coding: utf-8 -*-

import time, datetime, glob, os, sys, io, math
from collections import deque
import numpy as np
import pandas as pd
import curses
from curses import wrapper
import plotext as plx
from sparklines import sparklines
from pyfiglet import Figlet

import recordEEG as eeg

samples = 30


class Colors:
    delta     =   '\u001b[31m'
    theta     =   '\u001b[33m'
    lowAlpha  =   '\u001b[32m'
    highAlpha =   '\u001b[32;1m'
    lowBeta   =   '\u001b[36m'
    highBeta  =   '\u001b[36;1m'
    lowGamma  =   '\u001b[35m'
    midGamma  =   '\u001b[35;1m'
    reset     =   '\u001b[0m'    

def printf(txt,win,y=0,x=0):
    f = Figlet(font='smblock')
    for line in f.renderText(txt).split("\n"):
        win.addstr(y,x,line)
        win.clrtobot()
        y+=1

def powerbars(data, win, width, height):
  header = ['δ', 'θ', 'α', 'Α', 'β', 'Β', 'γ', 'Γ']
  data = np.array(data)[:,samples-1].tolist()
  #print(data)

  #win.addstr(str(data))
  #for line in sparklines(data, num_lines = height):
  #  win.addstr(str(line))

  for line in sparklines(data, num_lines = height):
    line = ''.join(Colors.delta + width * str(line[0]) +
      Colors.theta + width * str(line[1]) +
      Colors.lowAlpha + width * str(line[2]) +
      Colors.highAlpha + width * str(line[3]) +
      Colors.lowBeta + width * str(line[4]) +
      Colors.highBeta + width * str(line[5]) +
      Colors.lowGamma + width * str(line[6]) +
      Colors.midGamma + width * str(line[7])+ Colors.reset)
    #print(line)
    #win.addstr(str(line))
  #print(" " + "  ".join([g for g in header]))


class wincurses:
    def __init__(self, stdscr):

        ymin,xmin = 0,0
        ymax,xmax = stdscr.getmaxyx()

        self.time = curses.newwin(5, 30, 0, xmax-23)
        self.signal = curses.newwin(5,xmax-24,0,1)

        self.attn = curses.newwin(14,20,5,0)
        self.attn.addstr(0,2, "Attention: ")
        self.med = curses.newwin(14,20,6,0)
        self.med.addstr(0,2, "Meditation: ")

        self.powers = curses.newwin(10,26,7,0)
        self.powers.addstr(1,1," Delta: \n  Theta: \n  Low Alpha: \n  High Alpha: \n  Low Beta: \n  High Beta: \n  Low Gamma: \n  Mid Gamma: \n ")
        self.powers.box()

        self.stats_label = curses.newwin(11, 76, 7, 32)
        self.stats_label.addstr(0,6, "┌───────────────────────────────────────────────────────────────────┐")
        self.stats_label.addstr(1,6, "│   delta   theta   alpha   Alpha    beta    Beta   gamma   Gamma   │")
        self.stats_label.addstr(2,0, "┌─────\n│ log \n│ min \n│ max \n│ avg \n│ rng \n│ dif \n└─────  ")

        self.stats = curses.newwin(8, 69, 9, 38)
        self.stats.box()

        self.powerbars = curses.newwin(10,26,17,0)
        #self.powerbars.box()

        self.windows = [self.time, self.signal, self.attn, self.med, self.powers, self.stats_label, self.stats, self.powerbars]



def main(stdscr):

   max_height,max_width = stdscr.getmaxyx()

   while (True):
     try:

        win = wincurses(stdscr)
        data = eeg.Datapoints(eeg.get_samples())
        
	


        # Print Time & Signal
        printf(str(time.strftime('%H:%M:%S', time.gmtime(data.times[samples-1]))), win.time)
        printf(str(data.signals[samples-1]), win.signal)

        # Print Attn/Med
        win.attn.addstr(0,14, str(data.attns[samples-1]) + "\t")
        win.med.addstr(0,14,  str(data.meds[samples-1]) + "\t")

        # Print Powers
        line = 1
        for p in data.powers:
          win.powers.addstr(line,16,str(p[samples-1]) + "\t")
          line = line+1

        # Print powerbars
        powerbars(data.powers, win.powerbars, 3, 5)

        # Print Stats
        line = 1
        for stats in data.stats:
            s = " "
            for stat in stats:
                s = s + str("%6.3f" %stat.round(decimals=3) + "  ")
                win.stats.addstr(line,2,s)
            line = line+1

        # Refresh all windows (use noutrefresh and doupdate to prevent flickering)
        for w in win.windows:
            w.noutrefresh()
        curses.doupdate()

     # Error Handling (update this later to allow for lists < sample size)
     #except(ValueError, IndexError):
     #   stdscr.addstr(" wait.")
     #   stdscr.refresh()
     #   time.sleep(1)

     # Exit Program
     except(KeyboardInterrupt):
         curses.nocbreak()
         stdscr.keypad(False)
         curses.echo()
         curses.endwin()
         sys.exit()



if __name__ == '__main__':

  # OS friendly formatting
  os.system('cls' if os.name == 'nt' else 'clear')

  # find most recent folder and file
  dir = max([f.path for f in os.scandir('./EEG_data/') if f.is_dir()])
  file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)



  # get initial data frame
  #df = pd.read_csv(file,header=1)
  #header = list(df)

  # initialize curses with wrapper
  stdscr = curses.initscr()
  curses.noecho()
  curses.cbreak()
  curses.curs_set(0)
  #curses.start_color()
  stdscr.keypad(True)

  # MAIN
  wrapper(main(stdscr))

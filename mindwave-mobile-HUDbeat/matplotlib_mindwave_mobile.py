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

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from termgraph import termgraph as tg
import lehar        

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
  graph_data = open('/home/agoramachina/data/EEG_data/2019-08-06/EEGlog_00:41:57_2019-08-06.csv').read()
  lines = graph_data.split('\n')

  ts = []
  signals = []
  attns = []
  meds = []
  deltas = []
  thetas = []
  low_alphas = []
  high_alphas = []
  low_betas = []
  high_betas = []
  low_gammas = []
  mid_gammas = []

  for line in lines:
      if len(line) > 1:
          t, signal, attn, med, delta, theta, alpha_low, alpha_high, beta_low, beta_high, gamma_low, gamma_mid = line.split(',')
          ts.append(float(t))
          signals.append(float(signal))
          attns.append(float(attn))
          meds.append(float(med))
  ax1.clear()
  ax1.plot(ts, attns) 

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
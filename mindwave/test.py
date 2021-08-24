import time, datetime, os, sys, io, re, glob, math, csv, textwrap, bluetooth
from collections import deque

import numpy as np
import pandas as pd

from sparklines import sparklines

#Neurosky dependenies
from mindwavemobile.MindwaveDataPoints import *
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader

import recordEEG as eeg

print(eeg.get_samples())

print(eeg.Datapoints().times())
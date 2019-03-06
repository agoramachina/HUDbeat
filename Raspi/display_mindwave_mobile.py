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

# check for posix compatibility
if os.name != 'posix':
    sys.exit('{} platform not supported'.format(os.name))

# check for psutil
try:
    import psutil
except ImportError:
    print("The psutil library was not found. Run 'sudo -H pip install psutil' to install it.")
    sys.exit()

# Neurosky dependenies
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPoints import EEGPowersDataPoint
from mindwavemobile.MindwaveDataPoints import PoorSignalLevelDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader

# OLED SSD 1331 dependencies
from luma.oled.device import ssd1331
import luma.core.device
from luma.core.render import canvas
from luma.core.interface.serial import spi
from luma.core.virtual import terminal, viewport, snapshot, range_overlap
from luma.core.sprite_system import framerate_regulator
from PIL import Image, ImageDraw, ImageFont



# define folder and file names
## default folder name is:      /home/$user/data/EEG_data/yyyy-mm-dd
## defualt file name is:        EEGlog_hh:mm:ss_ yyyy-mm-dd.csv
foldername = "/home/" + getpass.getuser() + "/data/EEG_data/" + time.strftime("%Y-%m-%d/")
filename = foldername + "EEGlog_" + time.strftime("%H:%M:%S_%Y-%m-%d") + ".csv"

# if the folder doesn't exist, create it
if not os.path.exists(foldername):
    os.makedirs(foldername)

# OLED terminal font
def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)

# print EEG data to OLED terminal
def print_term(data_row):                
    term.println("delta: " + data_row[4])  #delta
    term.println("theta: " + data_row[5])  #theta
    term.println("alpha: " + data_row[6])  #low alpha
    term.println("Alpha: " + data_row[7])  #high alpha
    term.println("beta: " + data_row[8])   #low beta
    term.println("Beta: " + data_row[9])   #high beta
    term.println("gamma: " + data_row[10]) #low gamma
    term.println("Gamma: " + data_row[11]) #mid gamma
    term.println()

# print EEG data to OLED display
def draw_canvas(data_row):
    with canvas(device) as draw:

        draw.text((0,0),  data_row[4], fill="red", align="top") #delta
        draw.text((0,12), data_row[5], fill="yellow") #theta
        draw.text((0,24), data_row[6], fill="lime") #low alpha
        draw.text((0,36), data_row[7], fill="green") #high alpha
        draw.text((0,48), data_row[8], fill="blue") #low beta
        draw.text((0,60), data_row[9], fill="cyan") #high beta
        draw.text((0,72), data_row[10], fill="magenta") #low gamma
        draw.text((0,84), data_row[11], fill="purple") #mid gamma

def open_writer():
    # initialize writer
    with open(filename, "a") as f:
        writer = csv.writer(f)
        writer.writerow([current_datetime])
        writer.writerow(fields)

# MAIN FUNCTION
def main():

    #initialize OLED canvas
    canvas = luma.core.render.canvas(device)

    #define OLED fonts
    fonts = [make_font("code2000.ttf", 6) , device.width]

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
                    # print to terminal    
                    print(data_row)

                    # print to OLED terminal
                    #print_term(data_row)  
                    draw_canvas(data_row)                  
                    
                    # write to csv
                    with open(filename, "a") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_row)
                i = 1


# __MAIN__
# initialize mindwave reader
if __name__ == '__main__':


    # initialize OLED devices
    serial = spi(device=0,port=0)
    device = ssd1331(serial, rotate=1)
    device.width = 96
    device.height = 64

    # initialize OLED terminal and fonts
    term = terminal(device) 

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
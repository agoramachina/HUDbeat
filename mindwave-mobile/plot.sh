#!/bin/bash

cd ~/HUDbeat/mindwave-mobile/EEG_data/
ls -Art | tail -n 1

tail -f ./EEG_data/2019-10-30/EEGlog_20:22:45_2019-10-30.csv

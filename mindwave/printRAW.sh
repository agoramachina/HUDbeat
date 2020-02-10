#!/bin/bash
# @agoramachina 2019
#
# a bash script for reading, manipulating, and viewing
# live EEG data from a csv file.
# use while python graph_mindwave_mobilei.py is running

# set the sample rate
SAMPLE=10

#while true; do

	# get the most recently modified file in the EEG_data directory
	FOLDER=$(ls -td ~/HUDbeat/mindwave/EEG_data/*/ | head -1)
	FILE=$(ls -t $FOLDER/EEGlogRAW_* | head -1)
	tail -f -n1 $FILE
#sleep 1
#clear
#done


#!/bin/bash
# @agoramachina 2019
#
# a bash script for reading, manipulating, and viewing
# live EEG data from a csv file.
# use while python graph_mindwave_mobilei.py is running

# set the sample rate
SAMPLE=10

while true; do 

	# get the most recently modified file in the EEG_data directory
	FOLDER=$(ls -td ~/HUDbeat/mindwave-mobile/EEG_data/*/ | head -1)
	FILE=$(ls -t $FOLDER/EEGlog_* | head -1)
	
    	# define header names
    	HEAD=$(head -n 2 $FILE)
    	PHEAD=$(echo "delta,theta,alpha,Alpha,beta,Beta,gamma,Gamma")

	# get last N lines of csv data
	TAIL="$(tail $FILE -n1)"
	POWERS=$(echo "$(cut -d ',' -f 5- <<< "$TAIL")" | tr ',' ' ')
	ROW=$(tail $FILE -n1)
	POWER=$(cut -d ',' -f 5- <<< "$ROW" | tr ',' ' ')
	#echo "$POWER"
	sparklines $POWER
sleep 1
#clear
done


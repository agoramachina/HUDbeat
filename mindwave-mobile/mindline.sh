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
	
	SIGNAL=$(cut -d ',' -f 2 <<< "$TAIL")
	ATN=$(cut -d ',' -f 3 <<< "$TAIL")
	MED=$(cut -d ',' -f 4 <<< "$TAIL")

	
	POWERS=$(echo "$(cut -d ',' -f 5- <<< "$TAIL")" | tr ',' ' ')
	ROW=$(tail $FILE -n1)
	POWER=$(cut -d ',' -f 5- <<< "$ROW" | tr ',' ' ')
	#echo "$POWER"
	
	normal=$(tput sgr0)
	bold=$(tput bold)
	red=$(tput setaf 1)
	orange=$(tput setaf 16)
	yellow=$(tput setaf 3)
	green=$(tput setaf 2)
	blue=$(tput setaf 4)

	#printf "${blue}⊛${normal}"

#	if [ "$SIGNAL" -eq 0 ]; then
#    		printf "${green}⊕${normal} "; fi
#	if [ "$SIGNAL" -gt 0 ] && [ "$SIGNAL" -lt 50 ]; then
#		printf "${yellow}⊖${normal} "; fi
#	if [ "$SIGNAL" -gt 50 ] && [ "$SIGNAL" -lt 200 ]; then
#		printf "${orange}⊖${normal} "; fi
#	if [ "$SIGNAL" -eq 200 ]; then
#		printf "${red}⊗${normal} "; fi

	# TODO: add error handler for invalid data format
	sparklines $POWERS
sleep 1
#clear
done


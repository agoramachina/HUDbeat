#!/bin/bash
# @agoramachina 2019
#
# a bash script for reading, manipulating, and viewing
# live EEG data from a csv file.
# use while python graph_mindwave_mobilei.py is running

# set the sample rate
SAMPLE=10
RAWSAMPLE=60

while true; do 

	# get the most recently modified file in the EEG_data directory
	FOLDER=$(ls -td ~/HUDbeat/mindwave-mobile/EEG_data/*/ | head -1)
	FILE=$(ls -t $FOLDER/EEGlog_* | head -1)    	 
	RAWFILE=$(ls -t $FOLDER/EEGlogRAW* | head -1)

    	# define header names
    	HEAD=$(head -n 2 $FILE)
    	PHEAD=$(echo "delta,theta,alpha,Alpha,beta,Beta,gamma,Gamma")

	# get last N lines of csv data
	TAIL="$(tail $FILE -n$SAMPLE)"
	POWERS=$(echo "$(cut -d ',' -f 5- <<< "$TAIL")" | tr ',' '\t')
		    	
	# get the most recently written line in the csv file
	ROW=$(tail $FILE -n1)
	
	# define data variables
	TIME=$(cut -d ',' -f 1 <<< "$ROW")
	TIMES=$(cut -d ',' -f 1 <<< "$TAIL")
	SIGNAL=$(cut -d ',' -f 2 <<< "$ROW")
	
	ATTN=$(cut -d ',' -f 3 <<< "$ROW")
	MED=$(cut -d ',' -f 4 <<< "$ROW")
	
	DELTA=$(cut -d ',' -f 5 <<< "$ROW")
	THETA=$(cut -d ',' -f 6 <<< "$ROW")
	ALPHA_L=$(cut -d ',' -f 7 <<< "$ROW")
	ALPHA_H=$(cut -d ',' -f 8 <<< "$ROW")
	BETA_L=$(cut -d ',' -f 9 <<< "$ROW")
	BETA_H=$(cut -d ',' -f 10 <<< "$ROW")
	GAMMA_L=$(cut -d ',' -f 11 <<< "$ROW")
	GAMMA_M=$(cut -d ',' -f 12 <<< "$ROW")

	POWER=$(cut -d ',' -f 5- <<< "$ROW")
		
	# print data to terminal
	echo ---------------------
	echo '  ' Time:   $(date -ud @${TIME} +"%T")
	echo '  ' Signal: $SIGNAL
	echo '  ' Atn: $ATTN Med: $MED
	echo ---------------------
	echo
	echo $PHEAD | tr ',' '\t'
	#echo $POWER | tr ',' '\t'
	#echo
	echo "$POWERS"
	echo

	#for i in {1..8}; do
    	#	sparklines $(cut -f $i <<< "$POWERS")
	#done

	#echo "$POWERS" | tr '\t' ' '

	#awk '{ print $1 }' fs='\t' <<< $POWERS
	echo "$POWERS" > powers.dat
	RAWTAIL="$(tail $RAWFILE -n$RAWSAMPLE)"
	echo "$RAWTAIL" > raw.dat
	
sleep 1
clear
done


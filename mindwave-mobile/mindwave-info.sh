#!/bin/bash
# @agoramachina
# 2019-11-09
#
# a bash script for reading, manipulating, and viewing
# live EEG data from a csv file.
# use while python graph_mindwave_mobilei.py is running

while true; do

	# get the most recently modified file in the EEG_data directory
	FILE=$(find ~/HUDbeat/mindwave-mobile/EEG_data -type f -printf "%T@ %p\n" -ls \
	| sort -n | cut -d' ' -f 2- | tail -n 1)

	# get the most recently written line in the csv file
	ROW=$(tail $FILE -n1)
	
	# define data variables
	TIME=$(cut -d ',' -f 1 <<< "$ROW")
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

	SIGNAL=$(cut -d ',' -f 2 <<< "$ROW")
	ATNMED=$(cut -d ',' -f 3-4 <<< "$ROW")
	POWER=$(cut -d ',' -f 5- <<< "$ROW")
	
	echo Signal: $SIGNAL
	echo AtnMed: $ATNMED
	echo Powers: $POWER
	echo

	POWERS=($DELTA $THETA $ALPHA_L $ALPHA_H $BETA_L $BETA_H $GAMMA_L $GAMMA_M)

	echo LogPwr:
	for((i=0;i<8;i++))
	do
		#echo 'l(0)' | bc -l
    		echo ${POWERS[$i]} | cat
	done
	

#echo 'l(3) | bc -l

sleep 1
clear
done

#!/bin/bash
# @agoramachina
# 2019-11-09
#
# a bash script for reading, manipulating, and viewing
# live EEG data from a csv file
# use while python graph_mindwave_mobilei.py is running

while true; do

	# get the most recently modified file in the EEG_data directory
	FILE=$(find ~/HUDbeat/mindwave-mobile/EEG_data -type f -printf "%T@ %p\n" -ls \
	| sort -n | cut -d' ' -f 2- | tail -n 1)

	# get the most recently written line in the csv file
	ROW=$(tail $FILE -n1)
	ROW_CLEAN=$(echo $ROW | tr ',' ' ')
	echo $ROW_CLEAN
	
	#echo 'l(3) | bc -l

	# define signal, atnmed, powers
	SIGNAL=$(cut -d ',' -f 2 <<< "$ROW")
	ATNMED=$(cut -d ',' -f 3-4 <<< "$ROW")
	POWER=$(cut -d ',' -f 5- <<< "$ROW")
	echo Signal: $SIGNAL
	echo AtnMed: $ATNMED
	echo Powers: $POWER

	echo LogPwr:
	
	declare -a DATA[8]
	for ((i=1;i<=8;i++)); do
    		DATA=${(cut -d ',' -f $i <<< "$POWERS")}
    		echo DATA
    		#POWERS[i]=$("test $i")
	done
	echo $DATA[1]
	
	#awk -F',' '
	#{
	#    for (i=1;i<=8;i++)
	#    	print $i
	#}' <<< $POWERS
	
	#echo $LOGP
	#echo $POWERS|awk -F',' '{print $i}'

sleep 1
clear
done

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
	FILE=$(find ~/HUDbeat/mindwave-mobile/EEG_data -type f -printf "%T@ %p\n" -ls \
	| sort -n | cut -d' ' -f 2- | tail -n 1)

    	# define header names
    	HEAD=$(head -n 2 $FILE)
    	#PHEAD=$(cut -d ',' -f 5- <<< "$HEAD")
	PHEAD=$(echo "delta,theta,alpha,Alpha,beta,Beta,gamma,Gamma")

	# get last N lines of csv data
	TAIL="$(tail $FILE -n10)"
	PTAIL=$(cut -d ',' -f 5- <<< "$TAIL")
	PTAIL="$(echo "${PTAIL}" | tr ',' '\t')"
	echo "$PTAIL"
    	
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
	POWERS=($DELTA $THETA $ALPHA_L $ALPHA_H $BETA_L $BETA_H $GAMMA_L $GAMMA_M)
	declare -a POWER_LOGS

	# print data to terminal
	echo Signal: $SIGNAL
	echo AtnMed: $ATNMED
	echo
	echo $PHEAD | tr ',' '\t'
	echo $POWER | tr ',' '\t'
	echo

	echo LogPwr:

	#for i in ${POWERS[@]}
	for ((i=0;i<8;i++))
	do
    		echo -n $i
    		echo -e -n ' \t  '
    		echo ${POWERS[$i]}
    		#gnuplot -e "set terminal dumb; plot [-5:5] sin(x)"
    		#perl -e 'print log(22.0);'
		#echo 'l(0)' | bc -l
    		#echo ${POWERS[$i]} | cat
    		#echo 'L(${POWERS[$i]})' | bc -l
	#	POWER_LOGS=( "${arr[@]}" $i )
	#	echo -n $POWER_LOGS
		#echo  -n $i
    		#echo $POWER_LOGS[$i] | cat

    		
	done
	#echo ${POWERS[*]}
	#echo $POWERS[1]

	

#echo 'l(3) | bc -l

sleep 1
clear
done

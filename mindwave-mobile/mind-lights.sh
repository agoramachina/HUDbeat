#!/bin/bash
# @agoramachina 2019
#
# a bash script to change magic-home lights using Attn/Med data

FOLDER=$(ls -td ~/HUDbeat/mindwave-mobile/EEG_data/*/ | head -1)
FILE=$(ls -t $FOLDER/EEGlog_* | head -1)

IP=$(cut -d '|' -f 1 <<< "$(magic-home discover | grep 192)")
#echo "$IP"

DEVICES=()

for ip in $IP; do
    DEVICES+=("${ip}"); done

#declare -A DEVICES
echo "${DEVICES[@]} "
LOW=20
UNDER=40
OVER=60
HIGH=80

while true; do
	ATNMED[0]=$(cut -d ',' -f 3 <<< "$(tail $FILE -n1)")
	ATNMED[1]=$(cut -d ',' -f 4 <<< "$(tail $FILE -n1)")
	
	echo "${ATNMED[@]} "
	
	ATN="$(echo "2.55*"${ATNMED[0]}"" | bc)"
	MED="$(echo "2.55*"${ATNMED[1]}"" | bc)"

	echo "$ATN $MED "
	
	python -W ignore -m flux_led "${DEVICES[0]}" -c 0,"$ATN",0 >/dev/null
	python -W ignore -m flux_led "${DEVICES[1]}" -c 0,0,$MED >/dev/null
	
    	#if [ "${ATNMED[0]%.*}" -gt 60 ]; then
	#	python -W ignore -m flux_led "${DEVICES[0]}" -p 50 100 >/dev/null
	#fi
	
	sleep 1
	clear
done


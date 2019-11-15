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

while true; do
	ATN=$(cut -d ',' -f 3 <<< "$(tail $FILE -n1)")
	MED=$(cut -d ',' -f 4 <<< "$(tail $FILE -n1)")

	echo "$ATN $MED"

	ATNS="$(echo "2.55*"$ATN"" | bc)"
	MEDS="$(echo "2.55*"$MED"" | bc)"

	python -W ignore -m flux_led "${DEVICES[0]}" -c 0,$ATNS,0 >/dev/null
	python -W ignore -m flux_led "${DEVICES[1]}" -c 0,0,$MEDS >/dev/null
	sleep 1
	clear
done

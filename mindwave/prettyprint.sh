#/bin/bash
## @agoramachina 2020
#
# a bash script for displaying live EEG data all fancy like
#  use while recordEEG.py is running


# get the most recently modified file in the EEG_data directory
FOLDER=$(ls -td ~/HUDbeat/mindwave/EEG_data/*/ | head -1)
FILE=$(ls -t $FOLDER/EEGlog_* | head -1)
RAWFILE=$(ls -t $FOLDER/EEGlogRAW_* | head -1)

while true; do

	FILE=$(ls -t $FOLDER/EEGlog_* | head -1)
	tail -n1 $FILE | cut -d ',' -f2 -s | toilet -f smblock
	sleep 1
	clear
done

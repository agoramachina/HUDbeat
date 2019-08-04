import time
import bluetooth
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPoints import EEGPowersDataPoint
from mindwavemobile.MindwaveDataPoints import PoorSignalLevelDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
import textwrap
import datetime
import time
import re
import csv

if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    if (mindwaveDataPointReader.isConnected()):

        # initialize csv
        current_datetime = datetime.datetime.now().__str__()
        time_init = time.time()
        data_row = []
        fields = ['Time', 'Poor Signal Level', 'Attention', 'Meditation', 'Delta', 'Theta', 'Low Alpha', 'High Alpha', 'Low Beta', 'High Beta', 'Low Gamma', 'Mid Gamma']

        # write header row
        with open("EEG_output.csv", "a") as f:
          writer = csv.writer(f)
          writer.writerow([current_datetime])
          writer.writerow(fields)
        i = 0



        while(True):
            dataPoint = mindwaveDataPointReader.readNextDataPoint()
            if (not dataPoint.__class__ is RawDataPoint):
                data_cleaned = re.sub(r'[^\d\n]+', "", str(dataPoint))
                data_row.extend(data_cleaned.split())
                print(data_cleaned.split())


            with open("EEG_output.csv", "a") as f:
              writer = csv.writer(f)
              writer.writerow(data_row)
    else:
        print((textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " ")))
        

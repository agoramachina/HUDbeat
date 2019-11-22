# HUDbeat Mindwave

To be used with the Mindwave Mobile.

First, run the recordEEG program to generate data used by other programs:
    python recordEEG.py

By default, EEG logs are saved to './EEG_data/', relative to the folder the program is executed in. Raw signal data is saved in the format 'EEGlogRAW*.csv' and other data is saved as 'EEGlog*.csv'.


## mindline
A small bash script that prints a sparkline graph of live EEG power spectra. Can be used as a polybar module.


## TODO: todo

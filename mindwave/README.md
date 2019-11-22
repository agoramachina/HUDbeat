# HUDbeat Mindwave

To be used with the Mindwave Mobile.

First, run the recordEEG program to generate data used by other programs:
    python recordEEG.py

By default, EEG logs are saved to './EEG_data/' relative to the folder the program is executed in. Raw signal data is saved in the format 'EEGlogRAW*.csv'; other data is saved as 'EEGlog*.csv'.

recordEEG.py can be edited to exclude raw EEG writes if a smaller memory footprint is desired.

To plot EEG data, first run the plotEEG script:
    sh plotEEG.sh

This creates the 'raw.dat' and 'powers.dat' files inside the './EEG_plot/' directory, which can then be used by gnuplotlib and other applications to graph EEG data. Sample size can be set in 'plotEEG.sh'. This script must be running in order to generate live data for these applications!

## mindline
A small bash script that prints a sparkline graph of live EEG power spectra. Can be used as a polybar module.


## TODO: todo

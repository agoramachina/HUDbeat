# HUDbeat Mindwave

To be used with the Mindwave Mobile.


**First, run the recordEEG program** to generate data used by other programs:

    python recordEEG.py

By default, EEG logs are saved to `./EEG_data/` relative to the folder the program is executed in. Raw signal data is saved in the format `EEGlogRAW*.csv`; other data is saved as `EEGlog*.csv`.

recordEEG.py can be edited to exclude raw EEG writes if a smaller memory footprint is desired.


**To live plot EEG data in the terminal**, run one of the programs below:

    python stream_raw.py
    python stream_pow.py


**To plot EEG data with gnuplot**, first run the plotEEG script:

    sh plotEEG.sh

This creates the `raw.dat` and `powers.dat` files inside the `./EEG_plot/` directory, which can then be used by gnuplotlib and other applications to graph EEG data. Sample size can be set in `plotEEG.sh`. This script must be running in order to generate live data for these applications!

**To show a live graph** of the EEG power spectra over the last `n` samples (60 by default), run `plotpowers` while `plotEEG.sh` is running.

    gnuplot plotpowers.gnu


## mindline
A small bash script that prints a sparkline graph of live EEG power spectra. Calls tail -n1 of most recently modified EEG powers file. Can be used as a polybar module. Use while `recordEEG.py` is running.

Can also be run as a standalone script:

    sh mindline.sh

## mindlights
Uses live EEG data to control tintlink wifi led bulbs. 
I seem to have broken my bulbs running this, so USE AT YOUR OWN RISK!
Use while `recordEEG.py` is running.

    sh mindlights.sh

## midimind
Uses live EEG data to create music by generating MIDI signals from EEG signals! Use while `recordEEG.py` is running. Current WIP (2019-11-26).

    python midimind.py

## turtlewave
Uses live EEG data and the turtle python package to draw neat turtle graphics! Use while `recordEEG.py` is running.

    python turtlewave.py

## CHANGELOG
08-14-2021: added live terminal graphs and updated instructions

## TODO 
* midi
  - finally moving away from direct midi writes. let's pipe that through something fun instead, yeah? 
  - considering: `pure data`, `supercollider`, `sonic-pi`. probably going to go with `sonic-pi`.
  - listen for an updated file (or pipe), then pass that through osc. let the other programs handle the fancy stuff.
  - (plus, has the advantage of portability)
* more general optimization
* changelog?

## BUGS
* `curseEEG.py` doesn't play nicely if there are fewer samples than it expects. fix that.


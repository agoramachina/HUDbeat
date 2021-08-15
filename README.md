# HUDbeat
## A wearable Heads Up Display for biometric and environmental data


*__This project is a work in progress. HUDbeat is not intended as a medical device!__*

The goal of HUDbeat is to provide live biofeedback data through wearable technology.

In its first iteration, HUDbeat used an Adafruit Gemma M0 (and eventually a Trinket M0) with a Pulse Sensor Amped to gather heart rate data from the user's temple. This was sent to the internal Dotstar LED on a Gemma/Trinket M0 mounted to the user's glasses, which could be seen in the user's peripheral vision. 

In its current iteration (03-15-2019), HUDbeat uses a Raspberry Pi Zero W to detect and display live EEG data over Bluetooth from the Mindwave Mobile. It displays this data in realtime to an OLED while recording it as a .csv file to the Pi's SD card. SCAD cases (and corresponding .stl files) for hardware modules have been designed for the Gemma M0, Itsy Bitsy M4, Circuit Playground Express, and Adafruit's .96" color TFT, .96" color OLED, Arduino Spy Camera, SPI Bluetooth module, and 350 mAh lipo battery. 

Current updates (as of 11-21-2019) are focused on retreiving, manipulating, and displaying EEG data recorded from [Neurosky's Mindwave Mobile 2](https://store.neurosky.com/pages/mindwave).

As of 02-10-2020, live EEG data can be sent to turtles, midi, or smart lights.

As of 08-14-2021, data can now be live streamed and plotted on the terminal. Currently working on midi/osc/sound.


Future updates will focus on integrating the Pi with the Arduino and other modules.

.scad and .stl files can be found on agoramachina's Thingiverse page in the HUDbeat collection:
https://www.thingiverse.com/agoramachina/collections/hudbeat

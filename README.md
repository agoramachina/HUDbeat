# HUDbeat
## A wearable Heads Up Display for biometric and environmental data

** __This project is a work in progress. HUDbeat is not intended as a medical device!__ **

The goal of HUDbeat is to provide live biofeedback data through wearable technology.

In its first iteration, HUDbeat used an Adafruit Gemma MO (and eventually a Trinket M0) with a Pulse Sensor Amped to gather heart rate data from the user's temple. This was sent to the internal Dotstar LED on a Gemma/Trinket M0 mounted to the user's glasses, which could be seen in the user's peripheral vision. 

In its current iteration (02-27-2019), HUDbeat uses a Raspberry Pi Zero W to detect EEG data over Bluetooth from the Mindwave Mobile 2. SCAD cases (and corresponding .stl files) have been designed for the Gemma M0, Itsy Bitsy M4, Circuit Playground Express, and Adafruits .96" color TFT, .96" color OLED, Arduino Spy Camera, SPI Bluetooth module, and 350 mAh lipo battery. ~~Right now my files are all over the place, so the next few updates will focus on organizing those and uploading the .scad and .stl files.~~ (mostly complete).

Future updates will focus on integrating the Pi with the Arduino and other modules.

![](https://github.com/agoramachina/HUDbeat/blob/master/images/20190227_02.jpg)

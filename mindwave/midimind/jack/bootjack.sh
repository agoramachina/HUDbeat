#!/bin/bash

/usr/bin/jackd -d alsa -d hw:PCH -r 44000 -p 128 -n 2

#!/bin/bash

#set terminal dumb size 60, 20
#set autoscale
#set logscale

set logscale y
plot "powers.dat" using 0:1 with lines, \
"powers.dat" using 0:2 with lines, \
"powers.dat" using 0:3 with lines, \
"powers.dat" using 0:4 with lines, \
"powers.dat" using 0:5 with lines, \
"powers.dat" using 0:6 with lines, \
"powers.dat" using 0:7 with lines, \
"powers.dat" using 0:8 with lines, \
#set format x ''
#set format y ''
#unset xtics
#unset ytics
#unset border


pause 1
clear
reread

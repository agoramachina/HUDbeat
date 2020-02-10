set terminal dumb size 100,10

set logscale y
set format x ''; set format y '' 
unset xtics; unset ytics
unset key
unset border

plot "powers.dat" using 0:1 with lines
plot "powers.dat" using 0:2 with lines
plot "powers.dat" using 0:3 with lines
plot "powers.dat" using 0:4 with lines
plot "powers.dat" using 0:5 with lines
plot "powers.dat" using 0:6 with lines
plot "powers.dat" using 0:7 with lines
plot "powers.dat" using 0:8 with lines

pause 1
clear
reread

set terminal dumb #size 60, 20
set size 1,.5

set logscale y
set format x ''; set format y '' 
unset xtics; unset ytics
unset key
unset border

plot "powers.dat" using 0:1 with lines, \
"powers.dat" using 0:2 with lines

pause 1
clear
reread

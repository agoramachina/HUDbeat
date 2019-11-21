#set terminal dumb size 120,10

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

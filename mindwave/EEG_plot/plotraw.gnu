set terminal dumb size 100, 10

#set logscale y
set format x ''; set format y '' 
unset xtics; unset ytics
unset key
unset border

plot "raw.dat" using 0:1 with lines

pause .01
clear
reread

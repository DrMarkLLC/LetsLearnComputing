set term jpeg size 1920,1080 font 'arial,14'
set output 'avg-vs-3n^2.jpg'
plot 'avg.txt' with linespoints lc 'blue' lw 2 title 'avg', '3NSQ.txt' with linespoints lc 'red' lw 2 title '3n^2'
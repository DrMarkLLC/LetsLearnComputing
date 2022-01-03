set term jpeg size 1920,1080 font 'arial,14'
set output 'avg-vs-5n^2.jpg'
plot 'avg.txt' with linespoints lc 'blue' lw 2 title 'avg', '5NSQ.txt' with linespoints lc 'red' lw 2 title '5n^2'
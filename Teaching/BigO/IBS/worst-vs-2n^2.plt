set term jpeg size 1920,1080 font 'arial,14'
set output 'worst-vs-2n^2.jpg'
plot 'worst.txt' with linespoints lc 'blue' lw 2 title 'worst', '2NSQ.txt' with linespoints lc 'red' lw 2 title '2n^2'
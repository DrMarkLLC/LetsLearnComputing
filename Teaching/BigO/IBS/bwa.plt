set term jpeg size 1920,1080 font 'arial,14'
set output 'bwa.jpg'
plot 'best.txt' with linespoints lc 'green' lw 2 title 'best', 'avg.txt' with linespoints lc 'blue' lw 2 title 'avg', 'worst.txt' with linespoints lc 'red' lw 2 title 'worst'
set term jpeg size 1920,1080 font 'arial,14'
set output 'best-vs-3n.jpg'
plot 'best.txt' with linespoints lc 'blue' lw 2 title 'best', '3N.txt' with linespoints lc 'red' lw 2 title '3n'
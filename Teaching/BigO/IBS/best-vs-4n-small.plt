set term jpeg size 1920,1080 font 'arial,14'
set output 'best-vs-4n-small.jpg'
plot 'best-small.txt' with linespoints lc 'blue' lw 2 title 'best', '4N-small.txt' with linespoints lc 'red' lw 2 title '4n'
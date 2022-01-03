import sys

c = int(sys.argv[1])

for p in range(17):
    print(2**p, c * (2 ** p)**2)
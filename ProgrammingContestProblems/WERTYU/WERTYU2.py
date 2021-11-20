'''
Python solution to the WERTYU Kattis problem.

Version 2 - uses dictionary comprehension to build the map

Let's Learn Computing with Dr. Mark
2021-11-20
'''

import sys
# left to right, top to bottom string of all possible keys
keys = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

# build a dictionary that translates an input character to 
# one character left on the keyboard
map = {keys[i]:keys[i - 1] for i in range(1, len(keys))}

# the space character remains the same
map[' '] = ' '

# read all input in one statement
lines = sys.stdin.readlines()

# process each line 
for line in lines:
    # build a list of the new characters, based on old characters in 
    # the string, then stick all the new characters together for
    # printing
    print(''.join([map[ch] for ch in line[:-1]]))
'''
DELTA OMICRON permutation program. Randomly scramble the letters in 
DELTA OMICRON and split into two or three words, then output if they are
really words from a dictionary. 
'''
import random
import sys

# verify usage
if len(sys.argv) != 3:
    print('usage: python DeltaOmicron.py <out file name> <2|3|b>')
    exit()

# command-line parameter is output file name
outFileName = sys.argv[1]

# build a dictionary of correctly-spelled English words
with open('dictionary.txt', 'r') as dFile:
    dictionary = {word : 0 for word in dFile.read().split()}

# source 'delta omicron' letters to begin each permutation with
origString = 'deltaomicron'

# keep track of combinations seen to cut down on repeats
seenIt = {}

# build at most 100 permutations, echo to stdin and output file
with open(outFileName, 'w') as outFile:
    num = 0
    while num < 100:

        # 2 words
        if sys.argv[2] == '2' or sys.argv[2] == 'b':
            # split point
            point = random.randrange(0, len(origString))

            # permutation of whole string
            shufString = list(origString[:])
            random.shuffle(shufString)

            # cut into two words
            str1 = ''.join(shufString[:point])
            str2 = ''.join(shufString[point:])

            # real words? 
            if str1 in dictionary and str2 in dictionary:
                # new permutation?
                if (str1, str2) not in seenIt:
                    print(num, str1, str2)
                    outFile.write('{0:s} {1:s}\n'.format(str1, str2))
                    seenIt[(str1, str2)] = 0
                    seenIt[(str2, str1)] = 0
                    num += 1

        # 3 words -- similar process
        if sys.argv[2] == '3' or sys.argv[2] == 'b':

            # two split points
            p1 = random.randrange(0, len(origString))
            p2 = random.randrange(0, len(origString))
    
            shufString = list(origString[:])
            random.shuffle(shufString)
            str1 = ''.join(shufString[:p1])
            str2 = ''.join(shufString[p1:p2])
            str3 = ''.join(shufString[p2:])
            if str1 in dictionary and str2 in dictionary and str3 in dictionary:
                if (str1, str2, str3) not in seenIt:
                    print(num, str1, str2, str3)
                    outFile.write('{0:s} {1:s} {2:s}\n'.format(str1, str2, str3))
                    seenIt[(str1, str2, str3)] = 0
                    seenIt[(str1, str3, str2)] = 0
                    seenIt[(str2, str1, str3)] = 0
                    seenIt[(str2, str3, str1)] = 0
                    seenIt[(str3, str1, str2)] = 0
                    seenIt[(str3, str2, str1)] = 0
                    num += 1
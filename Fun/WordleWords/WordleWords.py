# get all 5-letter words from our dictionary of ~78,000 words
with open('../DeltaOmicron/dictionary.txt', 'r') as inFile:
    flws = [x[:-1] for x in inFile if len(x) == 6]

# find all 5-letter words that have as many "Wheel of Fortune" 
# letters as possible
wof = {'r', 's', 't', 'l', 'n', 'e'}
wofWords = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
maxLen = -1
for w in flws:
    wIntWof = set.intersection(wof, w)
    if len(wIntWof) > maxLen:
        maxLen = len(wIntWof)
    wofWords[len(wIntWof)].append(w)

print('Five-letter words with the most of {r, s, t, l, n, e}:')
for w in wofWords[maxLen]:
    print(w)

# find all 5-letter words with as many of the ohter vowels in them
other = {'a', 'i', 'o', 'u', 'y'}
otherWords = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
maxLen = -1
for w in flws:
    wIntOther = set.intersection(other, w)
    if len(wIntOther) > maxLen:
        maxLen = len(wIntOther)
    otherWords[len(wIntOther)].append(w)

print('Five letter words with the most of {a, i, o, u, y}:')
for w in otherWords[maxLen]:
    print(w)
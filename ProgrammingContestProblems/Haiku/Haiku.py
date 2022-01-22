'''
Python solution to the Haiku programming competition problem from Kattis.
'''
# read all the inputs
S = int(input())
syllables = [input() for i in range(S)]
s1 = input()
s2 = input()
s3 = input()

'''
Does a line have a certain number of syllables?

parameters
----------
  n - number of syllables line must have
  ln - line to check

returns
-------
  True if ln contains n syllables, False otherwise
'''
def hku(n, ln):
    # base case 1: used all syllables, but have more line
    if n < 0:
        return False
    # base case 2: used all syllables, and no line left
    elif n == 0 and len(ln) == 0:
        return True
    else:
        # general case: recurse for every syllable that starts the line
        for s in syllables:
            if ln.startswith(s):
                if hku(n - 1, ln[len(s):].strip()):
                    return True
        return False

# check the input and output results
if hku(5, s1) and hku(7, s2) and hku(5, s3):
    print("haiku")
else:
    print("come back next year")
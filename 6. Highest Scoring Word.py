"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""

#initial solution
def high(x):
    lst = x.split()
    ret = [0]*len(lst)
    
    for i in range(0, len(lst)):
        for j in range(0, len(lst[i])):
            ret[i]+= ord(lst[i][j])-96
            
    yahoo = list(zip(lst, ret))
    yahoo.sort(key=lambda x:x[1])
    return yahoo[-1][0]

#updated solution
def high(x):
    return max(x.split(), key=lambda word: sum(map(lambda c: ord(c)- 96, word)))


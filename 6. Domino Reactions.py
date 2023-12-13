"""
You're given a string of dominos. For each slot, there are 3 options:

"|" represents a standing domino

"/" represents a knocked over domino

" " represents a space where there is no domino

For example:

"||| ||||//| |/"
Tipping a domino will cause the next domino to its right to fall over as well, but if a domino is already tipped over, or there is a domino missing, the reaction will stop.
What you must do is find the resulting string if the first domino is pushed over. So in out example above, the result would be:

"/// ||||//| |/"
since the reaction would stop as soon as it gets to a space.
"""

#initial solution
def domino_falling(s):
    i=1
    while(i<len(s)):
        if (s[i] == "|"):    
            s[i] = "/"
            i+=1
        else:
            break            
    return s
            
def domino_reaction(s):
    ss = list(s)
    if len(ss) == 0:
        return ""
    if ss[0] == "|":
        ss[0]="/"
        ss=domino_falling(ss) 
    return ''.join(str(i) for i in ss)
#updated solution

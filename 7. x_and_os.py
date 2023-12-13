"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Example input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""

#initial solution
def xo(s):
    return s.count("x") + s.count("X") == s.count("o") + s.count("O") or (s.count("x") + s.count("X")== 0 and s.count("o") + s.count("O")  ==0):

#updated solution
def xo(s):
  return s.lower.count("x") == s.lower.count("o")

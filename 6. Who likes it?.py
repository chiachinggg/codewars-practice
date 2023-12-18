"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.
"""

#initial solution
def likes(names):
    if len(names)==0:
        return "no one likes this"
    elif len(names)>=4:
        return "{}, {} and {} others like this".format(names[0], names[1], str(len(names)-2))
    elif len(names)==3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    elif len(names)==2:
        return "{} and {} like this".format(names[0], names[1])
    else:
        return "{} likes this".format(names[0])

  #updated solution
def likes(names):
  #can use case
    n = len(names)
    return{
      0: "no one likes this",
      1: "{} likes this",
      2: "{} and {} like this",
      3: "{}, {} and {} like this",
      4: "{}, {} and {} others like this"
    }[min(4, n)].format(*names, others=n-2)

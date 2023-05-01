"""
comprehensions are concise syntax for describing lists, sets and dictionaries
list comprehension format: [expr(item) for item in iterable]
"""

from math import factorial

# create a list of words by splitting a string:
words = "This course is very good but also the pace of explaining concepts is very fast".split()

# make a list of lengths of the words in the previous list
words_length = [len(word) for word in words]

# find the number of decimal digits for each os the factorials from 1 to 20
no_of_digits = [len(str(factorial(x))) for x in range(20)]

# redo above, but also remove duplicates in above list with set comprehensions, however, unordered
eliminate_duplicates = {len(str(factorial(x))) for x in range(20)}


if __name__ == '__main__':
    print(words_length)
    print(f" List comprehension: {no_of_digits}, vs. set comprehension: {eliminate_duplicates}")
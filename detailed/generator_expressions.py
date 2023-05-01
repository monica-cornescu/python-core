"""
between generator and comprehensions: use the same syntax as comprehensions, but produce a generator:
(expr(item) for item in iterable)
"""

# specify a generator for the list of the first 1 million square numbers; none of the squares is created at this point
million_squares = (x*x for x in range (1, 1000001))

# check the type of the object
million_squares

# force evaluation of the generator
# create a list and display only the last 10 elements; consumes a lot of memory
list(million_squares)[-10:]

# calling again the list returns nothing because the generator was already created and exhausted
list(million_squares)

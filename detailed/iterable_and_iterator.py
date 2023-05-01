"""
learn about iteration protocol
an iterable (a collection or stream of objects, as a list) can be passed to iter() to produce an iterator
iterator objects support the iterator protocol; iterator objects can be passed to the next() function to fetch the next
value in the sequence
"""

# make an iterable source object, a list
iterable = ["Spring", "Summer", "Autumn", "Winter"]

# get an iterator from the iterable object
iterator = iter(iterable)

# request a value from the iterator, using next(); should give us Spring; calling this 4 times yields all 4 values;
# calling it the 5th time python raises an StopIteration exception
next(iterator)



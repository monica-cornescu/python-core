""" learn and practice with ranges and enumerations
a range is a collection rather than a container
range is used to produce consecutive integers for loop counts
"""

# range(stop)
print("range(5) starts with 0 and ends with 4", range(5))
for i in range(5):
    print(i)

# make a list of ints from 5 to 14 by using range(start, stop)
print(list(range(5, 10)) + list(range(10, 15)))

# make a list of even numbers from 0 to 8 using range(start, stop, count)
print(list(range(0, 10, 2)))


# if you need a counter, use enumerate - constructs an iterable series of pairs, each being a tuple (index, value)
t = [5, 22, 437, 59, 8]


if __name__ == '__main__':
    for p in enumerate(t):
        print(p)

    for i, v in enumerate(t):   # or use tuple unpacking
        print(f"i = {i}, v = {v}")
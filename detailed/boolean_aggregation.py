"""
iterator operations of boolean values iterable series
"""
from filter_comprehensions_is_prime import is_prime

# any takes an iterable and tells if any elements in it are True
any([False, False, True, False])

# all takes an iterable and tells if all elements in it are true
all([True, True, False, True])

# are any prime numbers in the range?
if any(is_prime(x) for x in range(1328, 1361)):
    print("Yes! There is at least 1 prime number in this range")
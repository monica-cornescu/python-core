"""
Common builtin iterator operations: enumerate() - produces integer indexes, sum() - for summation of numbers
itertools module
"""
from itertools import islice
from filter_comprehensions_is_prime import is_prime

# generator expression which yields a list of the first 1 mil square numbers
million_squares = (x * x for x in range(1, 1000001))

# calculate the sum of the first 1 mil square numbers:
# this is calculated very fast and consumes almost no memory, compared to list comprehension
sum(x * x for x in range(1, 1000001))

# compute the sum of prime numbers from the first 1000 numbers:
sum(x for x in range(1, 1001) if is_prime(x))

# get the first 1000 primes
islice(all_primes, 1000)
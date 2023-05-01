from math import sqrt
from pprint import pprint as pp


def is_prime(x):
    """
    returns True if no divisors were found for x
    """
    if x < 2:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


# make a list with the prime numbers < number 100
prime_num_before_100 = [x for x in range(101) if is_prime(x)]

# dictionary comprehension mapping numbers with 3 divisors to a tuple of the divisors
prime_square_divisors = {x*x: (1, x, x*x) for x in range(20) if is_prime(x)}

if __name__ == '__main__':
    print(prime_num_before_100)
    pp(prime_square_divisors)

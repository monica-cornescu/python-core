"""
Raising an exception interrupts the program flow and transfers control to an exception handler.
Exceptiom handlers are defined using try - except code blocks
Avoid catching programmer errors!
Generally thy not to catch TypeErrors!
Prefer built-in exception types whenever possible
"""
import sys


def sqrt(x):
    """
    calculated square roots
    :param x: the number for which the square root is to be computed
    :return: the square root of x
    :raises: ValueError: if x is negative
    """
    if x < 0:
        raise ValueError("Cannot compute square root of " f"negative number {x}")

    guess = x
    i = 0
    while guess * guess != x and i <= 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This will never be printed")
    except ValueError as e:
        print(e, file=sys.stderr)
    print("program execution continues normally here")


if __name__ == '__main__':
    main()

"""
Practice with exceptions, accessing exception objects
"""
import sys
from math import log

DIGIT_MAP = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
             'eight': '8', 'nine': '9'}


def convert(s):
    """ converting a string to an integer"""
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:  # exception handler takes a tuple of 2 exception types
        print(f"Conversion error: {e!r}",
              file=sys.stderr)  # !r is the repl representation of the value will be inserted in the print string
        # returns this: Conversion error: TypeError("'int' object is not iterable")
        #return -1
        raise   # without an argument re-raises the exception that's currently processed


# with convert returning -1 we cannot use the function in a math log function, we get a value error
# so we change return -1 with raising the exception

def string_log(s):
    v = convert(s)
    return log(v)


def main():
    number = convert(734)
    string_log(number)


if __name__ == '__main__':
    main()

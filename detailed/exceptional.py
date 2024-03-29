"""
Practice with exceptions, handling exceptions
"""
DIGIT_MAP = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
             'eight': '8', 'nine': '9'}


def convert(s):
    """ converting a string to an integer"""
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"Conversion succeeded! x = {x}")
    except (KeyError, TypeError):   # exception handler takes a tuple of 2 exception types
        print("Conversion failed!")   # we need a pass here if we remove the print
    return x


def convert2(s):
    """ another version of converting a string to an integer"""
    try:
        number = ''
        slist = str(s).split()   # whatever s is, make it a string and make a list of it
        for token in slist:
            number += DIGIT_MAP[token]
        return int(number)
        print(f"Conversion succeeded! x = {x}")
    except (KeyError, TypeError):
        return -1


if __name__ == '__main__':
    print(convert("one three three seven"))
    print(convert("one three three seven".split()))
    print(convert("twotwotwo".split()))
    print(convert(734))
    print(convert2("one three three seven"))
    print(convert2("oneonetwo"))
    print(convert2(734))


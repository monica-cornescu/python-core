"""
given a list of numbers and a number k, check if any 2 numbers in the list add up to k
From LinkedIn
"""


def check_if_add_up(numbers, k):
    for elem in numbers:
        if k - elem in numbers:
            return True, elem, k-elem
    return False


if __name__ == '__main__':
    print(f"The results is: {check_if_add_up([42, 1, 4, 2, 12, 40], 52)}")
    print(check_if_add_up([42, 1, 4, 2, 12, 40], 53))
    print(check_if_add_up([42, 1, 4, 2, 12, 9], 13))

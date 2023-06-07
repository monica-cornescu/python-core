"""
An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a
given series of numbers. You are provided with consecutive elements of an Arithmetic Progression.
There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been
given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will
never be the first or last one.

Example
find_missing([1, 3, 5, 9, 11]) == 7
"""


def find_missing(sequence):
    if sequence[0] <= sequence[1]:    # can replace this if-else with sequence.sort()
        pass
    else:
        sequence.reverse()
    a = sequence[1] - sequence[0]
    b = sequence[2] - sequence[1]
    if a > b:
        return sequence[0] + b
    elif b > a:
        return sequence[1] + a
    else:
        for i in range(3, len(sequence)):
            if sequence[i] > sequence[i - 1] + a:
                return sequence[i - 1] + a


if __name__ == "__main__":
    print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))
    print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))
    print(find_missing([3, 7, 11, 15, 23]))
    print(find_missing([16, 13, 10, 4, 1]))
    print(find_missing([37, 34, 31, 28, 25, 22, 19, 16, 13, 10, 4, 1]))
    print(find_missing([1, 3, 4, 6, 7, 8, 9]))

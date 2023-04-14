#!/usr/bin/env python
import unittest

# def solution(A):
#     sortedA = sorted(A)
#     positiveA = []
#     for elem in sortedA:
#         if elem > 0:
#             positiveA.append(elem)
#
#     for i in positiveA:
#         a = i
#         b = i + 1
#         if b > a + 1:
#             return a + 1


def get_smallest_positive_int(values):
    sorted_values = sorted(values)
    number = 1
    for elem in sorted_values:
        if elem == number:
            number += 1
        elif elem > number:
            break
    #
    return number

#***************************************************************************************

class Test(unittest.TestCase):
    def test_one_elem_list(self):
        ''''''

        # GIVEN
        A = [0]

        # WHEN
        b = get_smallest_positive_int(A)

        # THEN
        self.assertEqual(1, b)

    def test_complex_list(self):
        ''''''

        # GIVEN
        A = [17, 2, -14, 7, 4, 1]

        # WHEN
        b = get_smallest_positive_int(A)

        # THEN
        self.assertEqual(3, b)

#***************************************************************************************

if __name__ == '__main__':
    unittest.main()

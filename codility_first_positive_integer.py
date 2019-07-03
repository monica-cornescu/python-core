
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



def solution(A):
    sortedA = sorted(A)
    number = 1
    for elem in sortedA:
        if elem == number:
            number += 1
        elif elem > number:
            break
    #
    return number

#A = [17, 2, -14, 7, 4, 1]
A = [0]
b = solution(A)
print(b)


# multiply each element of a list with the elements of the second list to produce a 3rd list

li1 = [1, 2, 4, 8, 16]
li2 = {20, 10, 40, 50}
li3 = []
for nr in li1:
    for elem in li2:
        li3.append(nr * elem)
print('resulting list li3 is: ', li3)
print('li3 has %d elements' % (len(li3)))








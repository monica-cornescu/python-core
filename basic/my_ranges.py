# create a list from a simple range
r = range(15)
listx = list(r)
if 13 in r:
    print(listx)

# more complex ranges; take a slice of the list made of a range
other_r = range(-513, 20, 17)
if -218 not in other_r:
    print(list(other_r))
    print(list(other_r)[10:15])
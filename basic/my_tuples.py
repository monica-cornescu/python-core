tup1 = (422, 1236, 41, 17, 89, 8, 237)
tupi2 = (1118,)
stritup = ("insp", "passed", "invalid", "dropped", "transm", 'filtered', 'none-stst')

# tuple assignment/packing-unpacking; define a tuple of VARIABLES and assign it to a tuple of values; must have same number of elements
(stat1, stat2, stat3, stat4, stat5, stat6, stat7) = tup1
(sstat1, sstat2, sstat3, sstat4, sstat5, sstat6, sstat7) = stritup

le_tup = tup1 + tupi2
print(le_tup)

# verify the value mapping (variable assignment)
print(stat3)
print(sstat5)

mixtup = (77, 42, "lasa", ['s', 3, 14])
mixtup_list = mixtup[3]*3
mixtup_string = mixtup[2]*4
mixtup_number = mixtup[1]*10

print(mixtup_list)
print(mixtup_string)
print(mixtup_number)


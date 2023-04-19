""" learn more and practice with sets
Sets are unordered collections of unique elements: sets are mutable, but the elements in it are immutable
"""

# Create an empty set with set(), not with {} which is for dictionaries
a_set = set()
print(a_set, type(a_set))
# create a set from any iterable element; duplicates are discarded -> usage for sets
myset = set([44, 21, 7, 769, 56566, 21])
print(myset)

# iterable, but the order is arbitrary
for x in myset:
    if x > 25:
        print(x)

# test membership with is and is not:
if 7 in myset and 8 not in myset:
    print("7 is in myset, while 8 is not")

# add 1 element to a set:
myset.add(45)
myset.add(769)
print("45 should be added to the set, but 769 should not, because it already exists in the set", myset)

# add multiple elements in one go:
myset.update([43, 22, 107])
print("Add elements of a list to myset:", myset)
myset.update({15, 77, 22})
print("Now add elements of another set to myset:", myset)

# remove an element with remove: the element must exist, otherwise we get keyerror
myset.remove(21)
print("myset after removing 21:", myset)

# remove with discard: doesn't complain id element does not exist
myset.discard(33)
myset.discard(22)
print("22 was removed, but 30 did not exist, so no worries!", myset)

# create shallow copy with copy()
new_set1 = myset.copy()
if new_set1 == myset and new_set1 is not myset:
    print("new_set1 has the same elements as myset, cause it's its copy:", new_set1)

# create shallow copy with set
new_set2 = set(myset)
if new_set2 == myset and new_set2 is not myset:
    print("new_set2 has the same elements as myset, cause it's its copy:", new_set2)

# Sets algebra
blue_eyes = {"Olivia", "Harry", "Lily", "Jack", "Amelia"}
blond_hair = {"Harry", "Joshua", "Jack", "Amelia", "Mia"}
eats_pizza = {"Harry", "Amelia"}
drink_milk = {"Harry", "Lily", "Lola", "Amelia"}
blood_0 = {"Mia", "Joshua", "Lily", "Olivia"}
blood_A = {"Jack", "Amelia"}
blood_B = {"harry"}
blood_AB = {"Joshua", "Lola"}

# make a set union: collects elements that are in either or both sets
print(f"The union of {blue_eyes} and {blond_hair} are people with either blue_eyes or blond_hair or both",
      blue_eyes.union(blond_hair))
if blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes):
    print("the union operation is commutative!!!")

# the intersection of 2 sets returns the elements that are common to both sets, and it is also commutative
print(f"The intersection of {blue_eyes} and {blond_hair} are people with both blue_eyes and blond_hair",
      blue_eyes.intersection(blond_hair))
if blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes):
    print("the intersection operation is commutative!!!")

# difference: find elements which are in the first set and are not in the second; this is not commutative
x = blue_eyes.difference(blond_hair)
y = blond_hair.difference(blue_eyes)
print(f"The people which have blue_eyes but don't have blond_hair are: {x}")
if x != y:
    print(f"and the people with blond_hair which don't have blue_eyes are: {y}")

# find all elements from both sets that are not in both sets; it's commutative
z = blue_eyes.symmetric_difference(blond_hair)
w = blond_hair.symmetric_difference(blue_eyes)
if z == w:
    print(f"The people who either have blue_eyes but not blond_hair, or have blond_hair but not blue_eyes are: {z}")

# 3 Predicate methods
# check if one set is a subset of another
if eats_pizza.issubset(drink_milk):
    print("All the people who eat_pizza also drink_milk, and they are:", eats_pizza)

# Check if a set is a superset of another (includes all the elements of another)
if drink_milk.issuperset(eats_pizza):
    print(f"From all the people who drink_milk, {drink_milk} some also eat_pizza: {eats_pizza}")

# Test that 2 sets have no members in common
if blood_0.isdisjoint(blood_A) and blood_B.isdisjoint(blood_AB):
    print("This is normal, because a person has a single blood type")

if __name__ == "__main__":
    print("Practice more with string operations!")

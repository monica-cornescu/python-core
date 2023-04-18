""" practice with strings
1. concatenation and split
2. partition
3. format
4. f-string format
"""

import math
import json

# length of a string
print(len("this is quite a long course"))

# concatenation with + and augmented assignment might produce problems with temporaries for memory and allocations:
print("un" + "forget" + "able")

word = "inter"
word += "change"
word += "able"
print(word)

# Prefer concatenating strings with join
colors_string = ";".join(["red", "blue", "green", "yellow"])
print(colors_string)
colors_list = colors_string.split(";")
print(colors_list)
bedrijf = "".join(["jouw", "ICT", "vacature"])
print(bedrijf)

# partitioning produces a tuple, so it's often used in conjunction with tuple unpacking
words = "unforgetable".partition("forget")
print(words)
departure, separator, arrival = "London:Edinburgh".partition(":")
print(departure, arrival)
origin, _, destination = "Amsterdam-Paris".partition("-")   # _ is  for unused or dummy values; we don't want to capture the separator
print(origin, destination)

# only the first encounter 0f the separator is considered:
s = "crocodile"
print(s.partition("o"))

stringformatting_1 = "My {0}'s birthday is {1}. {0} was born in {2}".format("mom", "21st of May", 1945)
print(stringformatting_1)
stringformatting_2 = "My height and weight are {} m and {} kg".format(1.81, 64)
print(stringformatting_2)
position = "Current position is {latitude} {longitude}".format(latitude="60N", longitude="5E")
print(position)
galactic_position = "Galactic position is x={pos[0]},  y={pos[1]}, z={pos[2]}".format(pos=[65.2, 25.1, 82.2])
print(galactic_position)
math_constants = "Math constants are pi={m.pi} and e={m.e}".format(m=math)
print(math_constants)
math_constants_3f = "Math constants are pi={m.pi:.3f} and {m.e:.3f}".format(m=math)
print(math_constants_3f)

value = 4 * 20
forfstring = f'The results is {value}'   # value is evaluated and inserted at runtime
print(forfstring)


if __name__ == '__main__':
    print("Practice more with string operations!")
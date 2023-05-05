"""
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are
substrings of strings of a2.
Example 1:
a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns ["arp", "live", "strong"]

Example 2:
a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
Beware: In some languages r must be without duplicates.
"""


# put words in a set, to remove duplicates, then make a list of it and order it
def in_array(array1, array2):
    # s = set()
    # for word in array1:
    #     for long_word in array2:
    #         if word in long_word:
    #             s.add(word)
    # return sorted(s)
    words = []
    for word in array1:
        for long_word in array2:
            if word in long_word and word not in words:
                words.append(word)
    return sorted(words)


if __name__ == '__main__':
    print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
    print(in_array(["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))


# solutions from other people, without sets, so simpler, or with any:
def in_array01(array1, array2):
    # your code
    res = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2 and not a1 in res:
                res.append(a1)
    res.sort()
    return res


def in_array02(array1, array2):
    array2 = ' '.join(array2)
    return sorted(set(a for a in array1 if a in array2))


def in_array03(array1, array2):
    r = []
    for s1 in array1:
        for s2 in array2:
            if s1 in s2 and s1 not in r:
                r.append(s1)
    r.sort()
    return r


def in_array04(array1, array2):
    return sorted(
        x for x in set(array1)
        if any(x in y for y in array2))


# if __name__ == '__main__':
#     print(in_array02(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
#     print(in_array02(["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))

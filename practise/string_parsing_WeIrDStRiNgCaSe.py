"""
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even
indexed characters in each word upper cased, and all odd indexed characters in each word lower cased.
The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper
cased and you need to start over for each word.
The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there
are multiple words. Words will be separated by a single space(' ').
Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
"""


def to_weird_case(words):
    words_list = words.split()
    new_words_list = []
    for word in words_list:
        new_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        new_words_list.append(new_word)
    return " ".join(new_words_list)


if __name__ == '__main__':
    print(to_weird_case('Weird string case'))


# other people's, nicer solutions:
def to_weird_case01(string):
    answers = ''
    for word in string.split():
        for idx, char in enumerate(word):
            if idx % 2 == 0:
                answers += char.upper()
            else:
                answers += char.lower()
        answers += ' '
    return answers[:-1]


def to_weird_case02(string):
    newstring = ''
    i = True
    for char in string:
        if i == True:
            newstring += char.upper()
            i = False
        elif i == False:
            newstring += char.lower()
            i = True
        if char == " ":
            newstring += ""
            i = True
    return newstring


# wow, so....smart
def to_weird_case(string):
    return ' '.join([''.join([y.lower() if i % 2 else y.upper() for i, y in enumerate(x)]) for x in string.split()])

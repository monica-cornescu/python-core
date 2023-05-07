"""
Description
Middle Earth is about to go to war. The forces of good will have many battles with the forces of evil. Different races
will certainly be involved. Each race has a certain worth when battling against others. On the side of good we have the
following races, with their associated worth:
Hobbits: 1
Men: 2
Elves: 3
Dwarves: 3
Eagles: 4
Wizards: 10
On the side of evil we have:
Orcs: 1
Men: 2
Wargs: 2
Goblins: 2
Uruk Hai: 3
Trolls: 5
Wizards: 10
Although weather, location, supplies and valor play a part in any battle, if you add up the worth of the side of good
and compare it with the worth of the side of evil, the side with the larger worth will tend to win.

Thus, given the count of each of the races on the side of good, followed by the count of each of the races on the side
of evil, determine which side wins.

Input:
The function will be given two parameters. Each parameter will be a string of multiple integers separated by a single
space. Each string will contain the count of each race on the side of good and evil.
The first parameter will contain the count of each race on the side of good in the following order:
Hobbits, Men, Elves, Dwarves, Eagles, Wizards.
The second parameter will contain the count of each race on the side of evil in the following order:
Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.
All values are non-negative integers. The resulting sum of the worth for each side will not exceed the limit of a
32-bit integer.

Output:
Return "Battle Result: Good triumphs over Evil" if good wins, "Battle Result: Evil eradicates all trace of Good" if
evil wins, or "Battle Result: No victor on this battle field" if it ends in a tie.
"""


# def good_vs_evil(good, evil):
#     gl = good.split()
#     el = evil.split()
#     good_score = 1 * int(gl[0]) + 2 * int(gl[1]) + 3 * int(gl[2]) + 3 * int(gl[3]) + 4 * int(gl[4]) + 10 * int(gl[5])
#     evil_score = 1 * int(el[0]) + 2 * int(el[1]) + 2 * int(el[2]) + 2 * int(el[3]) + 3 * int(el[4]) + 5 * int(el[5]) + \
#                  10 * int(el[6])
#     if good_score > evil_score:
#         return "Battle Result: Good triumphs over Evil"
#     elif evil_score > good_score:
#         return "Battle Result: Evil eradicates all trace of Good"
#     else:
#         return "Battle Result: No victor on this battle field"

# def good_vs_evil(good, evil):
#     good_worth = [1, 2, 3, 3, 4, 10]
#     evil_worth = [1, 2, 2, 2, 3, 5, 10]
#
#     def change_to_int(scores):
#         """
#         this function first transforms the string of scores into a list of ints
#         """
#         s = scores.split()
#         for i in range(len(s)):
#             s[i] = int(s[i])
#         return s
#
#     def calculate_good_score():
#         g = change_to_int(good)
#         g_score = 0
#         for i in range(len(good)):
#             g_score += good_worth[i] * g[i]
#         return g_score
#
#     def calculate_evil_score():
#         e = change_to_int(evil)
#         e_score = 0
#         for i in range(len(evil)):
#             e_score += evil_worth[i] * e[i]
#         return e_score
#
#     def battle_result():
#         if g_score > e_score:
#             return "Battle Result: Good triumphs over Evil"
#         elif e_score > _score:
#             return "Battle Result: Evil eradicates all trace of Good"
#         else:
#             return "Battle Result: No victor on this battle field"


def good_vs_evil(good, evil):
    good_worth = [1, 2, 3, 3, 4, 10]
    evil_worth = [1, 2, 2, 2, 3, 5, 10]

    def calculate_score(score, worth):
        total_score = 0
        for i in range(len(worth)):
            total_score += worth[i] * int(score[i])
        return total_score

    def battle_result(good_score, bad_score):
        if good_score > bad_score:
            return "Battle Result: Good triumphs over Evil"
        elif good_score < bad_score:
            return "Battle Result: Evil eradicates all trace of Good"
        else:
            return "Battle Result: No victor on this battle field"

    return battle_result(calculate_score(good.split(), good_worth), calculate_score(evil.split(), evil_worth))


if __name__ == '__main__':
    print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
    print(good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0'))
    print(good_vs_evil('1 0 0 0 0 0', '1 0 0 0 0 0 0'))

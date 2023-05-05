def good_vs_evil(good, evil):
    gl = good.split()
    el = evil.split()
    good_score = 1 * int(gl[0]) + 2 * int(gl[1]) + 3 * int(gl[2]) + 3 * int(gl[3]) + 4 * int(gl[4]) + 10 * int(gl[5])
    evil_score = 1 * int(el[0]) + 2 * int(el[1]) + 2 * int(el[2]) + 2 * int(el[3]) + 3 * int(el[4]) + 5 * int(el[5]) + \
                 10 * int(el[6])
    if good_score > evil_score:
        return "Battle Result: Good triumphs over Evil"
    elif evil_score > good_score:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

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

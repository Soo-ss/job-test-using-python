from collections import Counter


def numPY1(s):
    c = Counter(s.lower())
    return c["y"] == c["p"]


def numPY2(s):
    return s.lower().count("p") == s.lower().count("y")


def solution(s):
    count_p = 0
    count_y = 0

    for item in s.lower():
        if item == "p":
            count_p += 1
        elif item == "y":
            count_y += 1

    # 이것도 0, 0으로 같으니깐 굳이 쓸필요없었음
    if count_p == 0 and count_y == 0:
        return True

    if count_p != count_y:
        return False

    return True


print(solution("Pyy"))
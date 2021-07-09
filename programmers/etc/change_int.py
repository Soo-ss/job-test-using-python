def strToInt(str):
    return int(str)


def solution(s):
    s = list(s)

    if s[0] == "-":
        del s[0]
        return -int("".join(s))

    return int("".join(s))


print(solution("-1234"))
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0


def solution(x):
    digit = 0

    for item in list(map(int, str(x))):
        digit += item

    if x % digit == 0:
        return True

    return False


print(solution(11))
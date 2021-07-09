import math

# 에라토스테네스의 체
def solution2(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def solution(n):
    return sum([1 for i in range(2, n + 1) if is_prime(i)])

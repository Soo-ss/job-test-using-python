def adder1(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


def adder2(a, b):
    return (abs(a - b) + 1) * (a + b) // 2


def solution(a, b):
    if a > b:
        a, b = b, a
    return sum([i for i in range(a, b + 1)])


print(solution(3, 3))

def solution(n):
    sqrt = n ** (1 / 2)

    if sqrt % 1 == 0:
        return int((sqrt + 1) ** 2)

    return -1


print(solution(121))
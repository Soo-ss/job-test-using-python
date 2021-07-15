def solution1(n):
    tmp = ""
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer


def solution(n):
    answer = 0
    digit = 1
    arr = []

    while n // 3 != 0:
        arr.append(n % 3)
        n //= 3
    arr.append(n)

    for item in reversed(arr):
        answer += item * digit
        digit *= 3

    return answer


print(solution(45))
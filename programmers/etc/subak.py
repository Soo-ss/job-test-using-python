def water_melon1(n):
    s = "수박" * n
    return s[:n]


def water_melon2(n):
    return "수박" * (n // 2) + "수" * (n % 2)


def water_melon3(n):
    return ("수박" * n)[0:n]


def solution(n):
    return "".join(["수" if i % 2 == 0 else "박" for i in range(n)])


print(solution(3))
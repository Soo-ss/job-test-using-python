def gcd(n, m):
    while m != 0:
        r = n % m
        n = m
        m = r
    return n


def lcm(n, m):
    return int(n * m / gcd(n, m))


def solution(n, m):
    return [gcd(n, m), lcm(n, m)]


print(solution(3, 12))

# 알고보니 그냥 수학문제였음
def solution(brown, yellow):
    x = (4 + brown + ((4 + brown) ** 2 - 16 * (brown + yellow)) ** 0.5) // 4
    y = (brown + yellow) // x
    return [max(x, y), min(x, y)]


print(solution(8, 1))
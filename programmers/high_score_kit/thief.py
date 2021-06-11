def solution(money):
    n = len(money)

    # 첫 집을 무조건 터는 경우
    # 동그랗게 배치되어 있으므로 마지막은 못턴다.
    d1 = [0] * n
    d1[0] = money[0]
    d1[1] = money[0]

    for i in range(2, n):
        d1[i] = max(d1[i - 1], d1[i - 2] + money[i])

    # 마지막 집을 무조건 터는 경우
    d2 = [0] * n
    d2[1] = money[1]

    for i in range(2, n):
        d2[i] = max(d2[i - 1], d2[i - 2] + money[i])

    return max(d1[-2], d2[-1])


solution([1, 2, 3, 1])
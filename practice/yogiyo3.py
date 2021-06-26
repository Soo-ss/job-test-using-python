# N보다 큰 정수중에서 두개의 연속된숫자를 포함하지 않는 것
# 연속된 숫자이므로 카운터 안먹힘

from collections import Counter


def solution(N):
    answer = 0

    while True:
        N += 1
        tmp = list(str(N))
        # key, value
        for k, v in Counter(tmp).most_common(1):
            if v == 1:
                return int("".join(tmp))
            else:
                continue
        N = int("".join(tmp))
        # print(N)

    return answer


# 44432 => 45010
print(solution(1765))
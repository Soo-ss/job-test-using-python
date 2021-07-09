# list로 감싸지 않아도 됩니다!!
# 맞아요 sorted하면 리스트로 반환해서 나와요
def solution2(n):
    return int("".join(sorted(str(n), reverse=True)))


def solution(n):
    return int("".join(sorted(list(map(str, str(n))), reverse=True)))


print(solution2(118372))
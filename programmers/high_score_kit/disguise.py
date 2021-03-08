def solution(clothes):
    answer = {}

    for item in clothes:
        if item[1] in answer:
            answer[item[1]] += 1
        else:
            answer[item[1]] = 1

    count = 1
    for i in answer.values():
        count *= i + 1

    # 모두 안입은 경우 제거
    # 공집합 뺌
    # (의상종류+1)을 모두 곱한 후 -1 << 이건 수학시간때 경우의 수 하면서 배웠을겁니다.. => 난 기억이 없는데
    return count - 1


print(
    solution(
        [
            ["yellowhat", "headgear"],
            ["bluesunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ]
    )
)

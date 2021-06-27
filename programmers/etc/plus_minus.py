def solution(absolutes, signs):
    answer = 0

    for item1, item2 in zip(absolutes, signs):
        if not item2:
            answer -= item1
        else:
            answer += item1
    return answer


solution([4, 7, 12], [True, False, True])

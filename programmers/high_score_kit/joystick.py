def solution(name):

    # 상하 조정으로 알파벳 바꾸기
    # 둘 중 더 가까운거
    change = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    # print(change)
    idx = 0
    answer = 0

    while True:
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0:
            return answer

        # 좌, 우 이동방향 정함
        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1

        # 위치(인덱스) 조정
        if left < right:
            answer += left
        else:
            answer += right

        if left < right:
            idx += -left
        else:
            idx += right


print(solution("JEROEN"))

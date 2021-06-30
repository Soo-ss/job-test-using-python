def solution(lottos, win_nums):
    # rank써서 함
    # rank = [6, 6, 5, 4, 3, 2, 1]
    answer = []
    zero_count = 0
    correct_count = 0

    zero_count = lottos.count(0)

    for item in win_nums:
        if item in lottos:
            correct_count += 1

    if zero_count == 0 and correct_count == 0:
        return [6, 6]

    if correct_count == 0:
        return [7 - zero_count, 6]

    return [7 - (zero_count + correct_count), 7 - correct_count]


print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
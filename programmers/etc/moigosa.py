arr = list(map(int, input().split()))


def solution(answers):
    answer = []

    # %5, %8, %10 이렇게 해도 됨
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    first_count = 0
    second_count = 0
    third_count = 0

    # enumerate쓰기
    # for index, item in enumerate(answers):
    #     print(index, item)

    for i in range(len(answers)):
        if first[i % 5] == answers[i]:
            first_count += 1
        if second[i % 8] == answers[i]:
            second_count += 1
        if third[i % 10] == answers[i]:
            third_count += 1

    count_dict = {1: first_count, 2: second_count, 3: third_count}
    top_score = max(count_dict.values())
    answer = [student for student, score in count_dict.items() if score == top_score]

    return answer


solution(arr)
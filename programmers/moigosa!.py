arr = list(map(int, input().split()))


def solution(answers):
    answer = []

    first = [1, 2, 3, 4, 5] * 8
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 5
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4

    first_count = 0
    second_count = 0
    third_count = 0

    for i in range(len(answers)):
        if first[i] == answers[i]:
            first_count += 1
        if second[i] == answers[i]:
            second_count += 1
        if third[i] == answers[i]:
            third_count += 1

    # print(first_count, second_count, third_count)

    if (
        first_count == second_count
        and second_count == third_count
        and first_count == third_count
    ):
        answer.append(1)
        answer.append(2)
        answer.append(3)
        return answer

    tmp = {
        "1": first_count,
        "2": second_count,
        "3": third_count,
    }

    sdict = sorted(tmp.items())
    print(sdict)
    for i in tmp.keys():
        answer.append(i)

    print(answer)
    return answer


solution(arr)
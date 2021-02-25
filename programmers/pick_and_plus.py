arr = list(map(int, input().split()))


def solution(numbers):

    # 2. 따라서 여기는 sort할 필요없음.
    numbers.sort()

    answer = []
    for i in range(len(numbers)):
        start_index = i
        for j in range(len(numbers)):
            if start_index > j:
                answer.append(numbers[start_index] + numbers[j])

    s = {x for x in answer}
    answer = list(s)
    # 1. set은 sort를 보장해주지 않으므로 맨 마지막에 정렬 해줘야함.
    answer.sort()
    return answer


def another_solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))


solution(arr)
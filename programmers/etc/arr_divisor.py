def solution2(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]


def solution(arr, divisor):
    answer = []

    for item in arr:
        if item % divisor == 0:
            answer.append(item)

    answer.sort()

    if answer == []:
        answer.append(-1)

    return answer


print(solution([5, 9, 7, 10], 5))
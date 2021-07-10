def solution(arr):
    answer = []

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            del arr[i]

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))

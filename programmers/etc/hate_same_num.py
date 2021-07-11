def no_continuous1(s):
    a = []
    for i in s:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a


def no_continuous2(s):
    result = []
    for c in s:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result


def solution(arr):
    answer = []
    answer.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i - 1] != arr[i]:
            answer.append(arr[i])

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))

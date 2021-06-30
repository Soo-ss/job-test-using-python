def solution(s):
    answer = ""
    arr = list(s)

    length = len(arr)
    print(length // 2)

    if length % 2 == 0:
        answer += arr[length // 2 - 1]
        answer += arr[length // 2]
        return answer

    answer += arr[length // 2]

    return answer


solution("abcde")
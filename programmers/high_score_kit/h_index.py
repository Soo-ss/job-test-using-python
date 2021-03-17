def solution(citations):
    citations.sort()
    length = len(citations)

    for i in range(length):
        if citations[i] >= length - i:
            return length - i

    return 0


print(solution([1, 1, 3, 5, 5, 5]))

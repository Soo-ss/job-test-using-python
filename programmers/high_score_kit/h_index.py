def solution(citations):
    answer = 0

    citations.sort()
    answer = citations[len(citations) // 2]
    print(answer)
    return answer


solution([1, 1, 3, 5, 5, 5])

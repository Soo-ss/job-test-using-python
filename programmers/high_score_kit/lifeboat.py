def solution(people, limit):
    people.sort()
    answer = 0

    i = 0
    j = len(people) - 1

    while i < j:
        # 기존 보트 개수에서 보트에 2명을 태울수있게하면
        if people[j] + people[i] <= limit:
            i += 1
            answer += 1

        j -= 1

    # 마지막에 빼면됨
    return len(people) - answer


print(solution([70, 50, 80, 50], 100))
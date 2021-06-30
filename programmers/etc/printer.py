def solution(priorities, location):
    answer = 0
    # my = priorities[location]
    result = []

    loc = [i for i in range(len(priorities))]
    # print(loc)
    # print(loc.pop(0))

    while len(priorities) != 0:
        # 이때 꺼내기
        if priorities[0] == max(priorities):
            result.append(loc.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))

    answer = result.index(location) + 1

    print(answer)
    return answer


solution([2, 1, 3, 2], 2)
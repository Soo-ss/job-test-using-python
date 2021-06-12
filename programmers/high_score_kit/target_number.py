def solution(numbers, target):
    first = [0]

    for i in numbers:
        child = []
        for j in first:
            child.append(j + i)
            child.append(j - i)
        # 부모 노드 업뎃
        first = child

    return first.count(target)


print(solution([1, 1, 1, 1, 1], 3))
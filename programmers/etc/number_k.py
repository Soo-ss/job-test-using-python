def solution(array, commands):
    answer = []

    i = -1
    j = -1
    k = -1
    tmp = []
    for total in commands:
        for index, item in enumerate(total):
            if index == 0:
                i = item
            if index == 1:
                j = item
            if index == 2:
                k = item

        tmp = sorted(array[i - 1 : j])
        answer.append(tmp[k - 1])

    print(answer)
    return answer


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
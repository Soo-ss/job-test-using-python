def sumMatrix(A, B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    return answer


def solution(arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        tmp = []
        for item in range(len(i)):
            tmp.append(i[item] + j[item])
        answer.append(tmp)

    return answer


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))

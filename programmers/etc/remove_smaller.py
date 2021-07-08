def solution(arr):
    arr.remove(min(arr))

    if arr == []:
        arr.append(-1)

    return arr


print(solution([4, 3, 2, 1]))

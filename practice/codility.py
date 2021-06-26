def solution(A):
    A.sort()
    num = 1

    for item in A:
        if item == num:
            num += 1

    return num


solution([-1, -3])
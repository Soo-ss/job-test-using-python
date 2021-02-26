def solution(numbers):

    arr = list(map(str, numbers))
    # print(arr)

    # 문제에서 1000이하라고 함
    arr.sort(key=lambda x: x * 3, reverse=True)

    # 000처리
    return str(int("".join(arr)))


solution([0, 5, 10, 15, 20])
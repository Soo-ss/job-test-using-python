def solution(n):
    answer = ""
    arr = ["1", "2", "4"]
    # num = ["4", "1", "2"]

    while n > 0:
        n -= 1
        answer = arr[n % 3] + answer
        n //= 3

    print(answer)
    return answer


solution(10)
import re


def solution1(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, "0")
        a12 = a12.replace("1", "#")
        a12 = a12.replace("0", " ")
        answer.append(a12)
    return answer


solution2 = lambda n, arr1, arr2: (
    [
        "".join(map(lambda x: "#" if x == "1" else " ", "{0:b}".format(row).zfill(n)))
        for row in (a | b for a, b in zip(arr1, arr2))
    ]
)


def solution3(n, arr1, arr2):
    answer = ["#"] * n
    for i in range(0, n):
        answer[i] = str(bin(arr1[i] | arr2[i]))[2:]
        answer[i] = re.sub("1", "#", "0" * (n - len(answer[i])) + answer[i])
        answer[i] = re.sub("0", " ", answer[i])
    return answer


def solution4(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = (
            str(bin(arr1[i] | arr2[i])[2:])
            .rjust(n, "0")
            .replace("1", "#")
            .replace("0", " ")
        )
        answer.append(a)
    return answer


def solution5(n, arr1, arr2):
    answer = []
    for index in range(0, n):
        answer.append(
            str(bin(arr1[index] | arr2[index] | pow(2, n)))
            .replace("0b1", "")
            .replace("1", "#")
            .replace("0", " ")
        )
        pass

    return answer


def to_binary(n, num):
    arr = []
    while num:
        arr.append(num % 2)
        num //= 2

    if len(arr) < n:
        for _ in range(n - len(arr)):
            arr.append(0)

    arr.reverse()

    return arr


def solution(n, arr1, arr2):
    answer = []

    for item1, item2 in zip(arr1, arr2):
        tmp = ""
        for i, j in zip(to_binary(n, item1), to_binary(n, item2)):
            tmp += "#" if i | j == 1 else " "

        answer.append(tmp)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
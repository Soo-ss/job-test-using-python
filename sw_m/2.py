"""
2 7 4
1 10
1 5
1 7
2 10
2 1
2 3
2 7

"""


def main():
    p, n, h = map(int, input().split())

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    # print(arr)
    count = [0] * 100
    for index, item in enumerate(arr):
        # print(index, item)
        if item[1] < h:
            count[item[0]] += item[1] * 1000

    # print("===============")
    for index, item in enumerate(count):
        if index == p + 1:
            break
        if index == 0:
            continue
        else:
            print(index, item)


if __name__ == "__main__":
    main()
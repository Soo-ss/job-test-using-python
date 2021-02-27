"""
10
3 5 -1 -2 4 4 3 -2 -3 -2

"""

from collections import deque


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    visited = [False] * n
    count = 0

    # 같은 숫자가 2개임
    start = arr[0]
    while True:
        v_index = arr.index(start)
        if not visited[v_index]:
            visited[v_index] = True
            start = arr[v_index + start]
            count += 1
        else:
            break
    print(count)


if __name__ == "__main__":
    main()
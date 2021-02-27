"""
8
1 3 10 9 6 2 3 2

"""

import heapq


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    # 8은 2의 3승

    heap = []
    for item in arr:
        heapq.heappush(heap, item)

    # print(heap)
    for i in range(0, len(arr) - n):
        heapq.heappop(heap)
        print(heap)


if __name__ == "__main__":
    main()
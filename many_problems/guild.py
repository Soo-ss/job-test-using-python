n = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 0
for i in arr:
    max_value = arr[len(arr) - 1]
    for j in range(max_value):
        del arr[len(arr) - 1 - j]

    result += 1

print(result)
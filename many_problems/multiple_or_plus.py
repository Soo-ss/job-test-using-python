arr = list(map(int, input()))

length = len(arr)
result = 1

# 0을 하나로 모으기
for index, item in enumerate(arr):
    if index == length - 1:
        break

    if arr[index] == 0 and arr[index + 1] == 0:
        del arr[index]

# 0이 있을때
if arr[0] == 0:
    result = arr[1]
    for index, item in enumerate(arr):
        if index == 0 or index == 1:
            continue
        result *= arr[index]
else:
    for index, item in enumerate(arr):
        result *= arr[index]

print(result)

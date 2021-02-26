arr = list(map(int, input()))

a = 0
b = 0

if arr[0] == 0:
    a += 1
else:
    b += 1

for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:
        if arr[i] == 0:
            a += 1
        else:
            b += 1

if a > b:
    print(b)
else:
    print(a)
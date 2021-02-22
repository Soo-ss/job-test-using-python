n = int(input())
direction = input().split()

x, y = 1, 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
offset = ["L", "R", "U", "D"]

for i in list(direction):
    for j in range(len(offset)):
        if i == offset[j]:
            tmp_x = x + dx[j]
            tmp_y = y + dy[j]

    if tmp_x < 1 or tmp_y < 1 or tmp_x > n or tmp_y > n:
        continue

    x, y = tmp_x, tmp_y

print(x, y)

# arr = list(sys.stdin.readline().rstrip())
def main():

    arr = list(map(str, input()))

    bomb = 0
    raser = 0

    for item in arr:
        if item == "(":
            bomb += 1
        else:
            raser += 1

    if bomb == raser:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()

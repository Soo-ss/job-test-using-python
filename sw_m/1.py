"""
# input

h g f w r
4
h g
h f
g r
g w

"""

"""
# output

h g r 
h g w 
h f 

"""


def main():
    skills = list(map(str, input().split()))
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(str, input().split())))

    print(arr)

    # print(x)


if __name__ == "__main__":
    main()
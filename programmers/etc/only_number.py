def solution(s):
    print(len(s))
    if len(s) != 4 or len(s) != 6:
        return False

    for item in s:
        if item.isalpha():
            return False

    return True


print(solution("1234"))
def alpha_string46_try(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6


def alpha_string46_regex(s):
    import re

    return bool(re.match("^(\d{4}|\d{6})$", s))


def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)


def solution(s):
    for item in s:
        if item.isalpha():
            return False

    if len(s) == 4 or len(s) == 6:
        return True

    return False


print(solution("1234"))
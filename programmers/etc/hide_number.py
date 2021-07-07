def hide_numbers(s):
    return "*" * (len(s) - 4) + s[-4:]


def solution(phone_number):
    return "".join("*" for _ in list(phone_number)[:-4]) + "".join(
        _ for _ in list(phone_number)[-4:]
    )


print(solution("01033334444"))
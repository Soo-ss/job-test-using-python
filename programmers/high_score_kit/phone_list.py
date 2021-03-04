def solution(phone_book):
    phone_book.sort()

    for i, j in zip(phone_book, phone_book[1:]):
        # print(i, j)
        if j.startswith(i):
            return False

    return True


print(solution(["12", "123", "1235", "567", "88"]))

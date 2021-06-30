# 이름 겹치면 2붙이기
# 가운데 이름 빼기
# 마지막 이름은 8글자
# last name에는 하이픈 포함될수 있음.
# name is 2 or 3 parts

# the function should return
# "john.doe@example.com; peter.parker@example.com;
# mary.watsonpa@example.com; john.doe2@example.com;
# john.doe3@example.com; jane.doe@example.com;
# peter.parker2@example.com"

from collections import Counter, defaultdict


def solution(S, C):
    answer = []
    arr = list(S.split("; "))
    C = C.lower()

    user_count = 1

    for item in arr:
        item = item.lower()
        tmp = list(item.split(" "))
        if len(tmp) == 2:
            # print(tmp[0], tmp[1])
            email_address = tmp[0] + "." + tmp[1]
            # for item in answer:
            #     if email_address == item.split("@")[0]:
            #         user_count += 1
            #         email_address += str(user_count)
            #         break
            answer.append(email_address + "@" + C + ".com")

        else:
            # print(tmp[0], tmp[1], tmp[2])
            # last name 하이픈 처리
            if "-" in tmp[2]:
                last = list(tmp[2].split("-"))
                # print(last)
                # print(len(last[0]))
                complete_last = last[0]
                if len(last[0]) >= 8:
                    continue
                else:
                    count = 8 - len(last[0])
                    # print(list(last[1]))
                    last_one_arr = list(last[1])
                    for i in range(count):
                        complete_last += last_one_arr[i]

                # print(complete_last)
                email_address = tmp[0] + "." + complete_last
                # for item in answer:
                #     if email_address == item.split("@")[0]:
                #         user_count += 1
                #         email_address += str(user_count)
                #         break
                answer.append(email_address + "@" + C + ".com")
            else:
                email_address = tmp[0] + "." + tmp[2]
                # for item in answer:
                #     if email_address == item.split("@")[0]:
                #         user_count += 1
                #         email_address += str(user_count)
                #         break
                answer.append(email_address + "@" + C + ".com")

    # print(Counter(answer))
    # for k, v in Counter(answer).most_common():
    #     print(k, v)

    return "; ".join(answer)


solution(
    "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker",
    "Example",
)

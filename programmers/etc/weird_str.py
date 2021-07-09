def toWeirdCase(s):
    return " ".join(
        map(
            lambda x: "".join(
                [a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]
            ),
            s.split(" "),
        )
    )


def solution(s):
    s = s.split(" ")
    answer = ""

    for item in s:
        idx = 0
        for word in item:
            if idx % 2 == 0:
                answer += word.upper()
            else:
                answer += word.lower()
            idx += 1

        answer += " "

    return answer[:-1]


print(solution("try hello world"))
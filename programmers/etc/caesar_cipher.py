def solution(s, n):
    s = list(s)

    # isupper, islower => 확인하는 문자열은 영문자만 확인하며
    # 그렇지 않은 한글이나 특수기호인 경우에도 False를 반환하게된다.
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord("A") + n) % 26 + ord("A"))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord("a") + n) % 26 + ord("a"))

    return "".join(s)


print(solution("a B z", 4))
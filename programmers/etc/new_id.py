import re


def solution(new_id):
    st = new_id
    st = st.lower()
    # 백슬래시+문자열이면 문자열 매칭이라는 뜻
    # re.sub(패턴, 바꿀문자열, 문자열, 바꿀횟수(optional))
    st = re.sub("[^a-z0-9\-_.]", "", st)
    st = re.sub("\.+", ".", st)
    st = re.sub("^[.]|[.]$", "", st)
    st = "a" if len(st) == 0 else st[:15]
    st = re.sub("^[.]|[.]$", "", st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3 - len(st))])
    return st

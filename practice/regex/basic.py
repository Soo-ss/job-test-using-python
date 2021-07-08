"""
메타문자 => . ^ $ * + ? { } [ ] \ | ( )
[abc] => a, b, c 중 한 개의 문자와 매치

[] 안에 -(하이픈) 사용하면 From-to이다. (범위)
[a-c] == [abc], [0-5] == [012345]

[a-zA-Z] => 알파벳 모두
[0-9] => 숫자

^은 not이다. [^0-9] => 숫자가 아닌 문자만 매치된다.

\d - 숫자와 매치, [0-9]와 동일한 표현식이다.
\D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
\s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
\S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
\w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
\W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.


a.b => a + 모든문자 + b
a[.]b => a + Dot(.)문자 + b

ca*t => a반복 횟수가 0부터 2억개까지 (ct, cat, caaat 모두 가능)
ca+t => a반복 횟수가 1부터이다. (ct는 안됨)

ca{2}t => c + a(반드시 2번 반복) + t
ca{2,5}t => c + a(2~5회 반복) + t

ab?c => a + b(있어도 되고 없어도 된다) + c => {0,1}

match()	=> 문자열의 처음부터 정규식과 매치되는지 조사한다.
search() => 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
"""
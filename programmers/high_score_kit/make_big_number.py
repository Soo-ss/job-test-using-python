def solution(number, k):
    stack = []

    for item in number:
        while stack and item > stack[-1]:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(item)

    if k > 0:
        for i in range(k):
            stack.pop()

    return "".join(stack)


print(solution("4177252841", 4))
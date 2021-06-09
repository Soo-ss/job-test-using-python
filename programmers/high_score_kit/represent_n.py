def solution(N, number):
    answer = 0
    possible_set = [0, [N]]
    if N == number:
        return 1
    for i in range(2, 9):
        case_set = []
        # 같은 숫자 반복되는거 555같은거 추가
        basic_num = int(str(N) * i)
        case_set.append(basic_num)

        # 사용되는 숫자의 횟수 구함
        # 절반 넘어가면 같은 결과만 나오므로 절반만 씀

        # i = 5
        # x 1 2
        # y 4 3

        # i = 6
        # x 1 2 3
        # y 5 4 3
        for i_half in range(1, i // 2 + 1):
            # x + y == i
            for x in possible_set[i_half]:
                for y in possible_set[i - i_half]:
                    # print(possible_set)
                    case_set.append(x + y)
                    case_set.append(x - y)
                    case_set.append(y - x)
                    case_set.append(x * y)
                    if y != 0:
                        case_set.append(x / y)
                    if x != 0:
                        case_set.append(y / x)

            if number in case_set:
                return i

            possible_set.append(case_set)

    return -1


solution(5, 12)
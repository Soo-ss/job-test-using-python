import math


def is_prime(number):
    if number == 0 or number == 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def solution(nums):
    answer = 0

    length = len(nums)

    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                # print(nums[i], nums[j], nums[k])
                if is_prime(nums[i] + nums[j] + nums[k]):
                    answer += 1

    return answer


solution([1, 2, 3, 4])

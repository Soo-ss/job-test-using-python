def solution(nums):
    answer = 0

    size = int(len(nums) / 2)
    nums = list(set(nums))

    answer = size if len(nums) >= size else len(nums)

    return answer


print(solution([3, 3, 3, 2, 2, 2]))

def solution(nums):
    if nums is None or len(nums) == 0:
        return []

    nums.sort()
    return nums

"""Given a list of numbers and a target, return the indices of the two numbers that add up to the target. Each input has exactly one answer, and you cannot use the same element twice.

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1] (because 2 + 7 = 9)
"""


def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left = left + 1
        else:
            right = right - 1
    return [-1, -1]  # nothing found


print(two_sum([2, 7, 11, 15], 9))

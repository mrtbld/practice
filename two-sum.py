# https://leetcode.com/problems/two-sum/
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#     Given nums = [2, 7, 11, 15], target = 9,
#
#     Because nums[0] + nums[1] = 2 + 7 = 9,
#     return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        # O(n*n)
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], i+1):
                if a + b == target:
                    return [i, j]

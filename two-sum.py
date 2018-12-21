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
    # t:O(n), s:O(n)
    def twoSum(self, nums, target):
        # t:O(n), s:O(n)
        inversed = dict((n, i) for (i, n) in enumerate(nums))
        # t:O(n), s:O(1)
        for i, n in enumerate(nums): # t:O(n)
            if target - n in inversed: # t:O(1)
                j = inversed[target - n] # t:O(1)
                if i != j:
                    return [i, j]

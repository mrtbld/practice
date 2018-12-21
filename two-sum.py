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
        inversed = dict()
        # t:O(n), s:O(n)
        for i, n in enumerate(nums): # t:O(n), s:O(n)
            if target - n in inversed: # t:O(1)
                j = inversed[target - n] # t:O(1)
                if i != j:
                    return [j, i]
            inversed[n] = i # t:O(1)

print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))

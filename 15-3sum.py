# https://leetcode.com/problems/3sum/
#
# 15. 3Sum
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# Example:
#
#     Given array nums = [-1, 0, 1, 2, -1, -4],
#
#     A solution set is:
#     [
#       [-1, 0, 1],
#       [-1, -1, 2]
#     ]

class Solution:
    # t:O(n³), s:O(1 + output)
    def threeSum(self, nums):
        """
        >>> _ = Solution()
        >>> _.threeSum([-1, 0, 1, 2, -1, -4])
        [(-1, -1, 2), (-1, 0, 1)]
        >>> _.threeSum(list(range(-2, 1000)))
        [(-2, -1, 3), (-2, 0, 2), (-1, 0, 1)]
        """
        tuples = set()
        for i, a in enumerate(nums): # t:O(n)
            for j, b in enumerate(nums[i + 1:], i + 1): # t:O(n)
                for c in nums[j + 1:]: # t:O(n)
                    if a + b + c == 0:
                        tuples.add(tuple(sorted([a, b, c])))
        return sorted(tuples)

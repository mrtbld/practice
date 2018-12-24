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
from collections import defaultdict

class Solution:
    # t:O(n²), s:O(n + output)
    def threeSum(self, nums):
        """
        >>> _ = Solution()
        >>> _.threeSum([-1, 0, 1, 2, -1, -4])
        [(-1, -1, 2), (-1, 0, 1)]
        >>> _.threeSum(list(range(-2, 10000)))
        [(-1, 0, 1), (-2, -1, 3), (-2, 0, 2)]
        """
        values_counts = defaultdict(int)
        for n in nums:
            values_counts[n] += 1
        triplets = set()
        for i, a in enumerate(nums): # t:O(n)
            for b in nums[i + 1:]: # t:O(n)
                n = -(a+b)
                count = values_counts[n]
                if n == a:
                    count -= 1
                if n == b:
                    count -= 1
                if count > 0:
                    triplets.add(tuple(sorted((n, a, b))))
        return list(triplets)

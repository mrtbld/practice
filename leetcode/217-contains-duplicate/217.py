# https://leetcode.com/problems/contains-duplicate/
#
# 217. Contains Duplicate
#
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
#
# Example 1:
#
#     Input: [1,2,3,1]
#     Output: true
#
# Example 2:
#
#     Input: [1,2,3,4]
#     Output: false
#
# Example 3:
#
#     Input: [1,1,1,3,3,4,3,2,4,2]
#     Output: true

class Solution:
    # t:O(n), s:O(n)
    def containsDuplicate(self, nums):
        """Return True if nums has duplicate values, False otherwise.

        >>> _ = Solution()
        >>> _.containsDuplicate([1,2,3,1])
        True
        >>> _.containsDuplicate([1,2,3,4])
        False
        >>> _.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
        True
        >>> _.containsDuplicate(list(range(10000000)))
        False
        >>> _.containsDuplicate([1] * 10000000)
        True
        """
        seen = set()
        for n in nums: # t:O(n)
            if n in seen: # t:O(1)
                return True
            seen.add(n) # t:O(1), s:O(n)
        return False

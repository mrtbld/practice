# https://leetcode.com/problems/contains-duplicate/
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
        seen = set()
        for n in nums: # t:O(n)
            if n in seen: # t:O(1)
                return True
            seen.add(n) # t:O(1), s:O(n)
        return False

print(Solution().containsDuplicate([1,2,3,1]), True)
print(Solution().containsDuplicate([1,2,3,4]), False)
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)
print(Solution().containsDuplicate(list(range(10000000))), False)
print(Solution().containsDuplicate([1] * 10000000), True)

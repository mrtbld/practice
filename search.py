# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Suppose an array sorted in ascending order is rotated at some pivot unknown to
# you beforehand, i.e. [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].
#
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
#     Input: nums = [4,5,6,7,0,1,2], target = 0
#     Output: 4
#
# Example 2:
#
#     Input: nums = [4,5,6,7,0,1,2], target = 3
#     Output: -1

class Solution:
    def search(self, nums, target):
        """Return the position of target in rotated sorted nums, or -1.

        >>> _ = Solution()
        >>> _.search([4,5,6,7,0,1,2], 0)
        4
        >>> _.search([4,5,6,7,0,1,2], 2)
        6
        >>> _.search([4,5,6,7,0,1,2], 4)
        0
        >>> _.search([4,5,6,7,0,1,2], 7)
        3
        >>> _.search([4,5,6,7,0,1,2], 3)
        -1
        """
        if not nums:
            return -1
        # List head is first part lowest, and is higher that every of second
        # part.
        pivot = nums[0]
        # Lower bound of the search space, included.
        min_i = 0
        # Upper bound of the search space, excluded.
        max_i = len(nums)
        # Choose is_to_the_right_of(), used as the binary search comparison
        # function, according to target position relative to pivot (i.e. in
        # which part it resides). This predicate takes an index of nums and
        # returns True if target is further right, i.e. further down the list,
        # and False otherwise.
        if target < pivot:
            # Target is in second part, so to the right of every element of
            # first part (i.e. higher than pivot), and to the right of every
            # element of second part that's lower than target.
            is_to_the_right_of = lambda i: nums[i] >= pivot or nums[i] < target
        else:
            # Target is in first part, so to the right of every element that's
            # both in first part too and lower than target.
            is_to_the_right_of = lambda i: nums[i] >= pivot and nums[i] < target
        while min_i != max_i:
            i = (min_i + max_i) // 2
            if nums[i] == target:
                return i
            if is_to_the_right_of(i):
                min_i = i + 1
            else:
                max_i = i
        return -1

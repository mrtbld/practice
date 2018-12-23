# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to
# you beforehand, i.e.  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2].
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
#     Input: [3,4,5,1,2]
#     Output: 1
#
# Example 2:
#
#     Input: [4,5,6,7,0,1,2]
#     Output: 0

class Solution:
    def findMin(self, nums):
        """Returns minimum value of given rotated sorted list nums using binary
        search.

        >>> Solution().findMin([3,4,5,1,2])
        1
        >>> Solution().findMin([4,5,6,7,0,1,2])
        0
        >>> N = 10000000
        >>> Solution().findMin(list(range(N//2, N)) + list(range(7, N//2)))
        7
        """
        if not nums:
            return None
        # List head is first part lowest, and is higher that every of second
        # part.
        pivot = nums[0]
        # Lower bound of the search space, included.
        min_i = 0
        # Upper bound of the search space, excluded.
        max_i = len(nums)
        while min_i != max_i:
            i = (min_i + max_i) // 2
            if nums[i] > pivot:
                # i is in first part.
                min_i = i + 1
            else:
                # i is in second part.
                max_i = i
        return nums[min_i]

# https://leetcode.com/problems/longest-consecutive-sequence/
#
# 128. Longest Consecutive Sequence
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
#     Input: [100, 4, 200, 1, 3, 2]
#     Output: 4
#     Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
#     Therefore its length is 4.

import numpy as np

class Solution:
    # t:O(n+k), s:O(k)
    # where k is the range of nums values
    def longestConsecutive(self, nums):
        """Return the length of the longest consecutive sequence of given array.

        >>> Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
        4
        >>> Solution().longestConsecutive([0])
        1
        >>> Solution().longestConsecutive([])
        0
        >>> Solution().longestConsecutive([1, 1, 2, 2, 3, 3])
        3
        >>> Solution().longestConsecutive(list(range(-10000, 10000)))
        20000
        """
        if not nums:
            return 0
        offset = -min(nums)
        marks = np.zeros(max(nums) + offset + 1, dtype=np.uint8)
        for n in nums:
            marks[n + offset] = 1
        length = 0
        max_length = 0
        for mark in marks:
            if not mark:
                length = 0
            else:
                length += 1
                max_length = max(max_length, length)
        return max_length

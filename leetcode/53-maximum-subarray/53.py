from collections import namedtuple
import sys

sys.setrecursionlimit(2100)

MaxSubArrayValues = namedtuple(
    'MaxSubArrayValues',
    ('max_left', 'max_right', 'whole', 'max'),
)

class Solution:
    def maxSubArray(self, nums):
        """Return highest subarray sum, among all subarrays of nums.

        >>> _ = Solution()
        >>> _.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> _.maxSubArray([-1])
        -1
        >>> _.maxSubArray([-1,1,-1])
        1
        >>> _.maxSubArray([-1,1,1,-1])
        2
        >>> _.maxSubArray([0,0,1,0])
        1
        >>> _.maxSubArray([-2,-1,-4,-2])
        -1
        >>> _.maxSubArray([31,-41,59,26,-53,58,97,-93,-23,84])
        187
        >>> _.maxSubArray(list(range(-1000, 1000)))
        499500
        """
        result = self.maxSubArrayAccumulator(nums)
        assert self.maxSubArrayDivideAndConquer(nums) == result
        return result

    # t:O(n), s:O(1)
    def maxSubArrayAccumulator(self, nums):
        if not nums:
            return None
        cur_sum = 0
        max_sum = nums[0]
        for n in nums: # t:O(n)
            cur_sum += n
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum

    def maxSubArrayDivideAndConquer(self, nums):
        if not nums:
            return None
        return self.maxSubArrayDivideAndConquerRecur(nums).max

    # t:O(n), s:O(n)
    def maxSubArrayDivideAndConquerRecur(self, nums):
        if len(nums) == 1:
            return MaxSubArrayValues(nums[0], nums[0], nums[0], nums[0])
        left = self.maxSubArrayDivideAndConquerRecur(nums[:len(nums)//2])
        right = self.maxSubArrayDivideAndConquerRecur(nums[len(nums)//2:])
        return MaxSubArrayValues(
            max_left=max(left.max_left, left.whole + right.max_left),
            max_right=max(right.max_right, right.whole + left.max_right),
            whole=left.whole + right.whole,
            max=max(left.max_right + right.max_left, left.max, right.max),
        )

# https://leetcode.com/problems/maximum-subarray/
#
# Given an integer array nums, find the contiguous subarray (containing at least
# one number) which has the largest sum and return its sum.
#
# Example:
#
#     Input: [-2,1,-3,4,-1,2,1,-5,4],
#     Output: 6
#     Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.

class Solution:
    # O(n³)
    def maxSubArray(self, nums):
        max_sum = None
        for i in range(len(nums)): # O(n)
            for j in range(i, len(nums)): # O(n)
                subarray_sum = sum(nums[i:j+1]) # O(n)
                if max_sum is None or subarray_sum > max_sum:
                    max_sum = subarray_sum
        return max_sum

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
print(solution.maxSubArray([-1]), -1)
print(solution.maxSubArray([-1,1,-1]), 1)
print(solution.maxSubArray([-1,1,1,-1]), 2)
print(solution.maxSubArray([0,0,1,0]), 1)
print(solution.maxSubArray(list(range(-1000, 1000))), int((1000*(1000-1))/2))

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
    # t:O(n), s:O(1)
    def maxSubArray(self, nums):
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

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
print(solution.maxSubArray([-1]), -1)
print(solution.maxSubArray([-1,1,-1]), 1)
print(solution.maxSubArray([-1,1,1,-1]), 2)
print(solution.maxSubArray([0,0,1,0]), 1)
print(solution.maxSubArray([-2,-1,-4,-2]), -1)
print(solution.maxSubArray(list(range(-1000, 1000))), int((1000*(1000-1))/2))

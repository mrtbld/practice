# https://leetcode.com/problems/maximum-product-subarray/
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
#
# Example 1:
#
#     Input: [2,3,-2,4]
#     Output: 6
#     Explanation: [2,3] has the largest product 6.
#
# Example 2:
#
#     Input: [-2,0,-1]
#     Output: 0
#     Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution:
    # t:O(n), s:O(1)
    def maxProduct(self, nums):
        if not nums:
            return None
        product = 1
        alt_product = None
        max_product = nums[0]
        for n in nums: # t:O(n)
            product *= n
            if product > max_product:
                max_product = product
            if alt_product is not None:
                alt_product *= n
                if alt_product > max_product:
                    max_product = alt_product
            elif product < 0:
                alt_product = 1
            if product == 0:
                alt_product = None
                product = 1
        return max_product

solution = Solution()
print(solution.maxProduct([2,3,-2,4]), 6)
print(solution.maxProduct([2,3,-2,4,4]), 16)
print(solution.maxProduct([2,3,-2,4,4,0,-5,-2]), 16)
print(solution.maxProduct([0,-2,0,1,-1]), 1)
print(solution.maxProduct([-2,0,-1]), 0)
print(solution.maxProduct([-2,0,-1,0,7]), 7)
print(solution.maxProduct([-2,-2,-2,-2,-2]), 16)
print(solution.maxProduct([2,-5,-2,-4,3]), 24)

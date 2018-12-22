# https://leetcode.com/problems/product-of-array-except-self/
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
#
# Example:
#
#     Input:  [1,2,3,4]
#     Output: [24,12,8,6]
#
# Note: Please solve it without division and in O(n).
#
# Follow up: Could you solve it with constant space complexity? (The output
# array does not count as extra space for the purpose of space complexity
# analysis.)

class Solution:
    # t:O(n), s:O(1 + output)
    def productExceptSelf(self, nums):
        products = [1] * len(nums) # t:O(n), s:O(output)
        left_product = 1
        right_product = 1
        for i, (n, m) in enumerate(zip(nums, reversed(nums))): # t:O(n), s:O(1)
            # Build products of all elements to the left of nums[i].
            products[i] *= left_product # t:O(1), s:O(1)
            left_product *= n
            products[-i-1] *= right_product # t:O(1), s:O(1)
            right_product *= m
        return products


solution = Solution()

print(solution.productExceptSelf([1,2,3,4]), [24,12,8,6])
print(solution.productExceptSelf([1,2,3,4,0]), [0,0,0,0,24])
print(solution.productExceptSelf([2,2,2,2]), [8,8,8,8])
print(len(solution.productExceptSelf([1]*10000)))

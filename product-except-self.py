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
    # t:O(n), s:O(n + output)
    def productExceptSelf(self, nums):
        left_product = 1
        left_products = []
        right_product = 1
        right_products = []
        for n in nums: # t:O(n)
            # Build products of all elements to the left of nums[i].
            left_products.append(left_product) # t:O(1), s:O(n)
            left_product *= n
        for n in reversed(nums): # t:O(n)
            # Build products of all elements to the right of nums[i].
            right_products.append(right_product) # t:O(1), s:O(n)
            right_product *= n
        # Multiply left and right products to get final products.
        return [a * b for a, b in zip(left_products, reversed(right_products))] # s:O(output)


solution = Solution()

print(solution.productExceptSelf([1,2,3,4]), [24,12,8,6])
print(solution.productExceptSelf([1,2,3,4,0]), [0,0,0,0,24])
print(solution.productExceptSelf([2,2,2,2]), [8,8,8,8])
print(len(solution.productExceptSelf([1]*10000)))

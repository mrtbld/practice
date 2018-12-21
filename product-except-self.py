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
    # t:O(n²), s:O(n)
    def productExceptSelf(self, nums):
        products = []
        for i in range(len(nums)): # O(n)
            product = 1
            for j, n in enumerate(nums): # O(n)
                if i != j:
                    product *= n
            products.append(product)
        return products


solution = Solution()

print(solution.productExceptSelf([1,2,3,4]), [24,12,8,6])
print(solution.productExceptSelf([1,2,3,4,0]), [0,0,0,0,24])
print(len(solution.productExceptSelf([1]*10000)))

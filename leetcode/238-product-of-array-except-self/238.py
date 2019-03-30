class Solution:
    # t:O(n), s:O(1 + output)
    def productExceptSelf(self, nums):
        """For each element in nums, return the product of every other elements.

        >>> _ = Solution()
        >>> _.productExceptSelf([1,2,3,4])
        [24, 12, 8, 6]
        >>> _.productExceptSelf([1,2,3,4,0])
        [0, 0, 0, 0, 24]
        >>> _.productExceptSelf([2,2,2,2])
        [8, 8, 8, 8]
        >>> _.productExceptSelf([1]*10000)[:10]
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        """
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

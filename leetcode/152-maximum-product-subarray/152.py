class Solution:
    # t:O(n), s:O(1)
    def maxProduct(self, nums):
        """Return highest subarray product, among all subarrays of nums.

        >>> _ = Solution()
        >>> _.maxProduct([2,3,-2,4])
        6
        >>> _.maxProduct([2,3,-2,4,4])
        16
        >>> _.maxProduct([2,3,-2,4,4,0,-5,-2])
        16
        >>> _.maxProduct([0,-2,0,1,-1])
        1
        >>> _.maxProduct([-2,0,-1])
        0
        >>> _.maxProduct([-2,0,-1,0,7])
        7
        >>> _.maxProduct([-2,-2,-2,-2,-2])
        16
        >>> _.maxProduct([2,-5,-2,-4,3])
        24
        """
        if not nums:
            return None
        max_product = nums[0]
        for l in (nums, reversed(nums)): # t:O(n), s:O(1)
            product = 1
            for n in l: # t:O(n)
                product *= n
                if product > max_product:
                    max_product = product
                if product == 0:
                    product = 1
        return max_product

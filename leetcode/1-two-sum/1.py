class Solution:
    # t:O(n), s:O(n)
    def twoSum(self, nums, target):
        """Return the positions of the two numbers in nums that add up
        to target.

        >>> _ = Solution()
        >>> _.twoSum([2, 7, 11, 15], 9)
        [0, 1]
        >>> _.twoSum([3, 2, 4], 6)
        [1, 2]
        """
        inversed = dict()
        # t:O(n), s:O(n)
        for i, n in enumerate(nums): # t:O(n), s:O(n)
            if target - n in inversed: # t:O(1)
                j = inversed[target - n] # t:O(1)
                if i != j:
                    return [j, i]
            inversed[n] = i # t:O(1)

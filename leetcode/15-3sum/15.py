class Solution:
    # t:O(n²), s:O(n + output)
    def threeSum(self, nums):
        """
        >>> _ = Solution()
        >>> _.threeSum([-1, 0, 1, 2, -1, -4])
        [(-1, -1, 2), (-1, 0, 1)]
        >>> _.threeSum(list(range(-2, 10000)) + [-3, -3])
        [(-3, -3, 6), (-3, -2, 5), (-3, -1, 4), (-3, 0, 3), (-3, 1, 2), (-2, -1, 3), (-2, 0, 2), (-1, 0, 1)]
        >>> _.threeSum([0] * 6000)
        [(0, 0, 0)]
        """
        seen = set() # s:O(n)
        triplets = set()
        for i, a in enumerate(nums): # t:O(n)
            for b in nums[i + 1:]: # t:O(n)
                n = -(a+b)
                if n in seen: # t:O(1)
                    triplet = [n, a, b]
                    triplet.sort()
                    triplets.add(tuple(triplet))
            seen.add(a) # t:O(1)
        return sorted(triplets)

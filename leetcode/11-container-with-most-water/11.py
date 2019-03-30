class Solution:
    # t:O(n), s:O(1)
    def maxArea(self, heights):
        """Return the size of the biggest rectangle formed by lines of
        given heights.

        >>> _ = Solution()
        >>> _.maxArea([1,8,6,2,5,4,8,3,7])
        49
        """
        if len(heights) < 2:
            return None
        max_volume = 0
        i = 0
        j = len(heights) - 1
        while i != j:
            max_volume = max(max_volume, (j - i) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_volume

# https://leetcode.com/problems/container-with-most-water/
#
# 11. Container With Most Water
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
# forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
#     8▔       █                   ▒
#     7▔       █░░░░░░░░░░░░░░░░░░░▒░░░░░░░█
#     6▔       █░░░▒░░░░░░░░░░░░░░░▒░░░░░░░█
#     5▔       █░░░▒░░░░░░░▒░░░░░░░▒░░░░░░░█
#     4▔       █░░░▒░░░░░░░▒░░░▒░░░▒░░░░░░░█
#     3▔       █░░░▒░░░░░░░▒░░░▒░░░▒░░░▒░░░█
#     2▔       █░░░▒░░░▒░░░▒░░░▒░░░▒░░░▒░░░█
#     1▔   ▒   █░░░▒░░░▒░░░▒░░░▒░░░▒░░░▒░░░█
#     0▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this
# case, the max area of water (blue section) the container can contain is 49.
#
# Example:
#
#     Input: [1,8,6,2,5,4,8,3,7]
#     Output: 49

class Solution:
    # t:O(n*k), s:O(n)
    def maxArea(self, heights):
        """Return the size of the biggest rectangle formed by lines of
        given heights.

        >>> _ = Solution()
        >>> _.maxArea([1,8,6,2,5,4,8,3,7])
        49
        """
        # min i and max i of all equal-or-taller lines, by height
        min_max_i = dict()
        for i, height in enumerate(heights):
            for lower_height in range(height, -1, -1):
                if lower_height in min_max_i:
                    min_max_i[lower_height][1] = i
                else:
                    min_max_i[lower_height] = [i, i]
        max_volume = 0
        for i, height in enumerate(heights):
            farthest_at_level = max(
                abs(i - min_max_i[height][0]),
                abs(i - min_max_i[height][1]),
            )
            max_volume = max(max_volume, height * farthest_at_level)
        return max_volume

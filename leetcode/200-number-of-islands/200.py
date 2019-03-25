# https://leetcode.com/problems/number-of-islands/
#
# 200. Number of Islands
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting adjacent
# lands horizontally or vertically. You may assume all four edges of the grid
# are all surrounded by water.
#
# Example 1:
#
#     Input:
#     11110
#     11010
#     11000
#     00000
#
#     Output: 1
#
# Example 2:
#
#     Input:
#     11000
#     11000
#     00100
#     00011
#
#     Output: 3

from collections import deque
from itertools import product

class Solution:
    # t:O(m*n), s:O(m*n)
    def numIslands(self, grid):
        """
        >>> Solution().numIslands((
        ...     ('1','1','1','1','0'),
        ...     ('1','1','0','1','0'),
        ...     ('1','1','0','0','0'),
        ...     ('0','0','0','0','0'),
        ... ))
        1
        >>> Solution().numIslands((
        ...     ('1','1','0','0','0'),
        ...     ('1','1','0','0','0'),
        ...     ('0','0','1','0','0'),
        ...     ('0','0','0','1','1'),
        ... ))
        3
        >>> Solution().numIslands([['1']*1000]*1000)
        1
        """
        if not grid or not grid[0]:
            return 0
        row_count = len(grid)
        col_count = len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = set()
        island_count = 0
        for start_node in product(range(row_count), range(col_count)):
            if grid[start_node[0]][start_node[1]] == '0' or start_node in visited:
                continue
            island_count += 1
            queue = deque([start_node])
            visited.add(start_node)
            while queue:
                i, j = queue.pop()
                for di, dj in directions:
                    x, y = i + di, j + dj
                    if (
                        0 <= x < row_count
                        and 0 <= y < col_count
                        and grid[x][y] == '1'
                        and (x, y) not in visited
                    ):
                        queue.appendleft((x, y))
                        visited.add((x, y))
        return island_count

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

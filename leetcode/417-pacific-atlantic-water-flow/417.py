from itertools import chain

class Solution:
    # t:O(m*n), s:O(m*n)
    def pacificAtlantic(self, matrix):
        """Returns the nodes from which water can flow to both the Pacific and
        the Atlantic.

        >>> matrix = (
        ...     (1, 2, 2, 3, 5),
        ...     (3, 2, 3, 4, 4),
        ...     (2, 4, 5, 3, 1),
        ...     (6, 7, 1, 4, 5),
        ...     (5, 1, 1, 2, 4),
        ... )
        >>> sorted(Solution().pacificAtlantic(matrix))
        [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)]
        >>> Solution().pacificAtlantic([])
        []
        >>> Solution().pacificAtlantic([[]])
        []
        >>> Solution().pacificAtlantic([[1]])
        [(0, 0)]
        >>> sorted(Solution().pacificAtlantic([[1] * 2] * 3))
        [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
        >>> sorted(Solution().pacificAtlantic([[3,3,3,3,3,3],[3,0,3,3,0,3],[3,3,3,3,3,3]]))
        [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 2), (1, 3), (1, 5), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)]
        """
        if not matrix or not matrix[0]:
            return []
        row_count = len(matrix)
        col_count = len(matrix[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        pacific_reach = set()
        atlantic_reach = set()
        pacific = (
            pacific_reach,
            chain(
                ((i, 0) for i in range(row_count)),
                ((0, j) for j in range(col_count)),
            ),
        )
        atlantic = (
            atlantic_reach,
            chain(
                ((i, col_count - 1) for i in range(row_count)),
                ((row_count - 1, j) for j in range(col_count)),
            ),
        )
        for visited, nodes in (pacific, atlantic):
            for start_node in nodes:
                if start_node in visited:
                    continue
                stack = [start_node]
                visited.add(start_node)
                while stack:
                    i, j = stack.pop()
                    height = matrix[i][j]
                    for di, dj in directions:
                        x, y = i + di, j + dj
                        if (
                            0 <= x < row_count
                            and 0 <= y < col_count
                            and matrix[x][y] >= height
                            and (x, y) not in visited
                        ):
                            stack.append((x, y))
                            visited.add((x, y))

        return list(pacific_reach & atlantic_reach)

# https://leetcode.com/problems/course-schedule/
#
# 207. Course Schedule
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
#
# Example 1:
#
#     Input: 2, [[1,0]]
#     Output: true
#     Explanation: There are a total of 2 courses to take. To take course 1 you
#     should have finished course 0. So it is possible.
#
# Example 2:
#
#     Input: 2, [[1,0],[0,1]]
#     Output: false
#     Explanation: There are a total of 2 courses to take. To take course 1 you
#     should have finished course 0, and to take course 0 you should also have
#     finished course 1. So it is impossible.
#
# Note:
#
# 1. The input prerequisites is a graph represented by a list of edges, not
#    adjacency matrices. Read more about how a graph is represented:
#    https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
# 2. You may assume that there are no duplicate edges in the input
#    prerequisites.

class Solution:
    # t:O(V+E), s:O(max(V²,V+E))
    def canFinish(self, numCourses, prerequisites):
        """Return whether the given prerequisites are valid, i.e. allow all
        courses to be finished. In other words, whether the dependency graph has
        directed cycles or not. I.e. is a DAG or not.

        >>> Solution().canFinish(2, [[1,0]])
        True
        >>> Solution().canFinish(2, [[1,0],[0,1]])
        False
        >>> Solution().canFinish(7, [[0,1],[0,2],[4,3],[4,6],[6,3],[3,2]])
        True
        >>> Solution().canFinish(7, [[0,1],[0,2],[4,3],[4,6],[6,3],[3,2],[2,4]])
        False
        """
        adjacency_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjacency_list[a].append(b)

        m = {}
        def canFinishRecur(node):
            if node in m:
                return m[node]
            m[node] = {node}
            ancestors = set()
            for n in adjacency_list[node]:
                n_ancestors = canFinishRecur(n)
                if n_ancestors is None:
                    m[node] = None
                    return None
                ancestors |= n_ancestors
            if node in ancestors:
                m[node] = None
                return None
            ancestors.add(node)
            m[node] = ancestors
            return ancestors

        for node in range(len(adjacency_list)):
            if canFinishRecur(node) is None:
                return False
        return True

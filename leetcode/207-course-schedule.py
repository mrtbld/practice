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
        recur_result = self.canFinishRecur(numCourses, prerequisites)
        iter_result = self.canFinishIter(numCourses, prerequisites)
        assert recur_result == iter_result
        return recur_result

    # t:O(V+E), s:O(V+E)
    def canFinishRecur(self, numCourses, prerequisites):
        adjacency_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjacency_list[a].append(b)

        # 0: not visited, 1: visiting, 2: visited
        marks = [0] * numCourses
        def _canFinishRecur(node):
            if marks[node] == 2:
                return True
            if marks[node] == 1:
                return False
            marks[node] = 1
            all_ancestors_can_finish = all(_canFinishRecur(n) for n in adjacency_list[node])
            marks[node] = 2
            return all_ancestors_can_finish

        return all(_canFinishRecur(n) for n in range(numCourses))

    # t:O(V+E), s:O(V+E)
    def canFinishIter(self, numCourses, prerequisites):
        adjacency_list = [[] for _ in range(numCourses)]
        back_adjacency_counts = [0] * numCourses
        for a, b in prerequisites:
            adjacency_list[a].append(b)
            back_adjacency_counts[b] += 1

        stack = [node for node, count in enumerate(back_adjacency_counts) if count == 0]

        # Iterate in topological order.
        while stack:
            node = stack.pop()
            for n in adjacency_list[node]:
                back_adjacency_counts[n] -= 1
                if back_adjacency_counts[n] == 0:
                    stack.append(n)

        # If any backward edges remain, this indicates the presence of directed
        # cycles, thus the dependency graph is not a DAG, thus it is not
        # possible to satisfy every course prerequisites.
        return not any(back_adjacency_counts)
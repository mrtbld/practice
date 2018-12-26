# https://leetcode.com/problems/clone-graph/
#
# 133. Clone Graph
#
# Given the head of a graph, return a deep copy (clone) of the graph. Each node
# in the graph contains a label (int) and a list (List[UndirectedGraphNode]) of
# its neighbors. There is an edge between the given node and each of the nodes
# in its neighbors.

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node, m=None):
        if node is None:
            return None
        if m is None:
            m = dict()
        if node in m:
            return m[node]
        clone = UndirectedGraphNode(node.label)
        m[node] = clone
        clone.neighbors = []
        for n in node.neighbors:
            clone.neighbors.append(self.cloneGraph(n, m))
        return clone

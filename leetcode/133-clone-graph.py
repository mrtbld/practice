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
    def cloneGraph(self, node):
        if node is None:
            return None
        clones = {
            node: UndirectedGraphNode(node.label),
        }
        stack = [node]
        while stack:
            n = stack.pop()
            for neighbor in n.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = UndirectedGraphNode(neighbor.label)
                    stack.append(neighbor)
                clones[n].neighbors.append(clones[neighbor])
        return clones[node]

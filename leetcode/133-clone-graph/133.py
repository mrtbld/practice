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

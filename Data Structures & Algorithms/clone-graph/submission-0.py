from collections import defaultdict

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        neighbour_map = defaultdict(set)
        node_map = {}
        stack = [node]
        while stack:
            n = stack.pop()
            node_map[n.val] = Node(val=n.val)
            neighbour_map[n.val].update(neighbour.val for neighbour in n.neighbors)

            for neighbour in n.neighbors:
                if neighbour.val not in node_map:
                    stack.append(neighbour)
        
        for val, n in node_map.items():
            n.neighbors = [node_map[v] for v in neighbour_map[val]]
        
        return node_map[node.val]
            
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        oldToNew = dict()
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copied = Node(node.val, [])
            oldToNew[node] = copied
            
            for nei in node.neighbors:
                copied.neighbors.append(dfs(nei))
                
            return copied
        return dfs(node)
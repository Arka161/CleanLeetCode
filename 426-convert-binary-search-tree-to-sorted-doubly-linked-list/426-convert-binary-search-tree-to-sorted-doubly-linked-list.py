"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def __init__(self):
        self.head = None
        self.prev = None
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        self.treetoDoublyHelper(root)
        self.prev.right = self.head
        self.head.left = self.prev 
        return self.head

    def treetoDoublyHelper(self, node):
        if not node:
            return
        
        self.treetoDoublyHelper(node.left)
        if self.prev:
            node.left = self.prev
            self.prev.right = node
        else:
            self.head = node
        self.prev = node
        self.treetoDoublyHelper(node.right)
            
        
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root) :
        if not root:
            return None
        
        queue = [root]
        
        while queue:
            next_level = []
            for i in range(len(queue)):
                node = queue[i]
                if i < len(queue) - 1:
                    node.next = queue[i + 1]
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
        
        return root
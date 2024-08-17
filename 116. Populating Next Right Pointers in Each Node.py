"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root) :
        if not root:
            return root

        queue = [(root, 0)]
        prev_node_by_level = {}

        while queue:
            node, level = queue.pop(0)

            if level in prev_node_by_level:
                prev_node_by_level[level].next = node

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

            prev_node_by_level[level] = node

        return root
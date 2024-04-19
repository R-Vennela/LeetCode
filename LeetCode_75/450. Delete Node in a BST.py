# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def successor(node):
            node = node.right
            while node.left:
                node = node.left
            return node.val
        def predessor(node):
            node = node.left
            while node.right:
                node = node.right
            return node.val
        if not root:
            return root
        if root.val<key:
            root.right = self.deleteNode(root.right, key)
        elif root.val>key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right and not root.left:
                root = None
            elif root.right:
                root.val = successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = predessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
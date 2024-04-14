# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if not root:
            return sum
        elif not (root.left or root.right):
            return sum
        if root.left and not (root.left.left or root.left.right):
            sum += root.left.val
        return sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
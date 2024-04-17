# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.results = []

        def fun(node, res):
            if node.left:
                fun(node.left, res + chr(97 + node.val))
            if node.right:
                fun(node.right, res + chr(97 + node.val))  
            if not node.left and not node.right:
                res += chr(97 + node.val) 
                self.results.append(res[::-1])        


        fun(root, '')
        self.results.sort()
        return self.results[0]
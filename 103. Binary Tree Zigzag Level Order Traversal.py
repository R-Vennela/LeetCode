# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        b=[root]
        res=[]
        flag=True
        while b:
            val=[]
            b1=[]
            for i in b:
                val.append(i.val)
                if i.left:
                    b1.append(i.left)
                if i.right:
                    b1.append(i.right)
            if flag:
                res.append(val)
                flag=False
            else:
                res.append(val[::-1])
                flag=True
            b=b1
        return res

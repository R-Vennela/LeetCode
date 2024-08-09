# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root) :
        if not root: return []
        res=[[root.val]]
        q=deque()
        q.append(root)
        while q:
            temp=[]
            for i in range(len(q)):
                curr=q.popleft()
                if curr.left:
                    temp.append(curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    temp.append(curr.right.val)
                    q.append(curr.right)
            if len(temp)>0:
                res.append(temp)
        return res[::-1]
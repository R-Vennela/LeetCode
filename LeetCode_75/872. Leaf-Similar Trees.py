# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2) :
        seq1 = []
        seq2 = []

        self.buildSeq(root1, seq1)
        self.buildSeq(root2, seq2)

        return seq1 == seq2

    def buildSeq(self, root, seq):
        if root is None:
            return
        if root.left is None and root.right is None:
            seq.append(str(root.val))
            return
        self.buildSeq(root.left, seq)
        self.buildSeq(root.right, seq)
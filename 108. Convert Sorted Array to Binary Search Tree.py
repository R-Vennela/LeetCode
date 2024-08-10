#Python Code
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(arr, s, e):
            if s > e:
                return None
            mid = s + (e - s) // 2
            node = TreeNode(arr[mid])
            node.left = helper(arr, s, mid - 1)
            node.right = helper(arr, mid + 1, e)
            return node
        
        n = len(nums)
        if n == 0:
            return None
        return helper(nums, 0, n - 1)
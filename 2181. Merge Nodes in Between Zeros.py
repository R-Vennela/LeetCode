# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head):
        ptr1 = head
        ptr2 = head.next
        s = 0
        while ptr2:
            if ptr2.val == 0:
                ptr1 = ptr1.next
                ptr1.val=s
                s=0
            else:
                s+=ptr2.val
            ptr2 = ptr2.next
        ptr1.next=None
        return head.next
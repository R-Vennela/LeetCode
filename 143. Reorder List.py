# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head.next:
            return head
        prev=None
        slow=head
        fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None


        prev=None
        while (slow):
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp
        second = slow if slow!=None else prev


        curr=head
        prev=None
        while (curr):
            tmp1=curr.next
            tmp2=second.next
            prev=second
            curr.next=second
            second.next=tmp1
            curr=tmp1
            second=tmp2
        if second!=None:
            prev.next=second
        return head 
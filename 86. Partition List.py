# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head, x) :
        fdum, bdum = ListNode(0), ListNode(0)
        front, back, curr = fdum, bdum, head
        while curr:
            if curr.val < x:
                front.next = curr
                front = curr
            else:
                back.next = curr
                back = curr
            curr = curr.next
        front.next, back.next = bdum.next, None
        return fdum.next
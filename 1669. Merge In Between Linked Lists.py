# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        current = list1
        for _ in range(a-1):
            current = current.next

        l1 = current
        for _ in range(b-a+2):
            current = current.next

        l2 = current
        l1.next = list2
        current = list2

        while current.next:
            current = current.next

        current.next = l2
        return list1       
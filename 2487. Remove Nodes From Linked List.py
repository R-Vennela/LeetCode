# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #reverse the linked list
        prev=None
        curr=head
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        #traverse and find max value 
        maxVal=0
        head=prev
        curr=prev
        while(curr):
            nextNode=curr.next
            if(curr.val<maxVal):
                prev.next=nextNode
            else:
                maxVal=curr.val
                prev=curr

            curr=nextNode
        
        prev=None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev
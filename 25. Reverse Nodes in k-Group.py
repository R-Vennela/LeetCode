class Solution(object):
    def reverseKGroup(self, head, k):
        def reverseLinkedList(head,k):
            prev, curr = None, head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev, curr
        
        list_count = 0 # counts the no. of Nodes
        curr = head
        while curr:
            list_count += 1
            curr = curr.next
        
        dummy = ListNode(-1)
        prev_end = dummy
        
        loop_count = list_count // k  # How many parts Linked list should be broken and reversed
        curr = head
        
        for _ in range(loop_count):
            start = curr
            end, next_start = reverseLinkedList(curr, k)
            prev_end.next = end
            start.next = next_start
            prev_end = start
            curr = next_start
        
        return dummy.next
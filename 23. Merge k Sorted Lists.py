class Solution(object):
    def mergeKLists(self, lists):
        h = []
        for x in lists:
            pointer = x
            while pointer:
                heappush(h,pointer.val)
                pointer = pointer.next

        head = ListNode(0)
        curr = head
        while len(h) != 0:
            curr.next = ListNode(heappop(h))
            print(curr.val)
            curr = curr.next
        return head.next
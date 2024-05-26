class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        M = (10 ** 9) + 7
        l0a0 = 1
        l1a0 = 0
        l2a0 = 0
        l0a1 = 0
        l1a1 = 0
        l2a1 = 0

        for _ in range(n):
            l0a0, l0a1, l1a0, l2a0,  l1a1, l2a1 = (l0a0 + l1a0 + l2a0) % M,  (l0a1 + l1a1 + l2a1 + l0a0 + l1a0 + l2a0) % M, l0a0, l1a0, l0a1, l1a1
         
        return (l0a0 + l1a0 + l2a0 + l0a1 + l1a1 + l2a1) % M
class Solution:
    def minOperations(self, nums, k) :
        ans = 0
        for x in nums:
            ans ^= x
        ans ^= k
        res = 0
        while ans > 0:
            if (ans & 1) != 0:
                res += 1
            ans >>= 1
        
        return res  
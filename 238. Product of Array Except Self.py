class Solution:
    def productExceptSelf(self, nums) :
        n = len(nums)
        right = [0] * n
        res = [0] * n
        
        prod = 1
        for i in range(n - 1, -1, -1):
            prod *= nums[i]
            right[i] = prod

        prod = 1
        for i in range(n - 1):
            lp = prod
            rp = right[i + 1]

            res[i] = rp * lp
            prod *= nums[i] 

        res[n - 1] = prod
        return res
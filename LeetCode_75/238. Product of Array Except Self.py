class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prod_w_zeroes = 1
        zero_count = 0
        ans = [0]*n
        for x in nums:
            if x == 0:
                zero_count += 1
            else:
                prod_w_zeroes *= x

        for i in range(n):
            if nums[i] == 0:
                if zero_count>1:
                    ans[i] = 0
                else:
                    ans[i] = prod_w_zeroes
            if nums[i]!=0:
                if zero_count>=1:
                    ans[i] = 0
                else:
                    ans[i] = int(prod_w_zeroes/nums[i])

        return ans
class Solution:
    def findMaxK(self, nums) :
        res = -1
        nums = set(nums)
        for num in nums:
            if num * -1 in nums:
                res = max(res, num)
        return res
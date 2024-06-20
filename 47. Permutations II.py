class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        instances = {}
        res = []

        for num in nums:
            if num in instances:
                instances[num] += 1
            else:
                instances[num] = 1
        
        
        def rec(curArr):
            if len(curArr) == len(nums):
                res.append(curArr)
                return
            
            for i in instances:
                if instances[i] > 0:
                    instances[i] -= 1
                    rec(curArr + [i])
                    instances[i] += 1
            
        rec([])
        return res
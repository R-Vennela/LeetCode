class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
            for i in range(start, end):
                # swap the current element with the start
                nums[start], nums[i] = nums[i], nums[start]
                # continue with the next element
                backtrack(start + 1, end)
                # backtrack: swap back
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack(0, len(nums))
        return result
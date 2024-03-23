class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l = 0
        r = len(nums)-1
        max_operations = 0
        while l < r:
            if(nums[l] + nums[r] == k):
                max_operations += 1
                l = l+1
                r = r-1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return max_operations     
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        mini_pos = -1
        maxi_pos = -1
        last_out_pos = -1
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == minK:
                mini_pos = i
            if num == maxK:
                maxi_pos = i
            if num < minK or num > maxK:
                last_out_pos = i
                mini_pos = -1
                maxi_pos = -1
            
            if mini_pos != -1 and maxi_pos != -1:
                ans += min(mini_pos, maxi_pos) - last_out_pos
        
        return ans 
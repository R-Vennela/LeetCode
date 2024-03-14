class Solution:
    def numSubarraysWithSum(self, nums, goal) :
        result = 0
        prefix_sum = 0
        mp = {0: 1}
        for num in nums:
            prefix_sum += num
            result += mp.get(prefix_sum - goal, 0)
            mp[prefix_sum] = mp.get(prefix_sum, 0) + 1
        return result
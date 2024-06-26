class Solution:
        
    def combinationSum2(self, nums, target):
        
        def dfs(i, path, current_target):
            if(current_target == 0): # target was reached
                ans.append(path[:])
            else:
                for j in range(i,len(nums)):
                    if(j!=i and nums[j-1] == nums[j]):  # remove the duplicates
                        continue

                    if(current_target < nums[j]):
                        break

                    dfs(j+1, path + [nums[j]], current_target - nums[j])
            
        ans = []
        nums.sort()
        dfs(0,[],target)
        return ans
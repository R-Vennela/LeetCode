class Solution:
    def moveZeroes(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        L, R = 0, len(nums)-1

        while L <= R:
            while nums[R] == 0 and L<=R:
                R-=1
            
            while nums[L] == 0 and L <= R:
                temp = nums.pop(L)
                nums.insert(R, temp)
                R-=1
            else:
                L+=1 
#class Solution(object):
 #   def findKthLargest(self, nums, k):
  #      size=len(nums)
   #     array = [None for _ in range(size)]
    #    for i in range(len(nums)):
     #       maxi=max(nums)
      #      array[i]=maxi
       #     nums.remove(maxi)
            
        #return array[k-1]


class Solution(object):
   def findKthLargest(self, nums, k):
    nums.sort()
    return nums[len(nums)-k]
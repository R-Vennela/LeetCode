class Solution(object):
    def isPossible(self,nums,day,m,k):
        count=0
        dupm=0
        for i in nums:
            if i<=day:
                count+=1
            else:
                dupm+=(count//k)
                count=0
        dupm+=(count//k)
        if m<=dupm:
            return True
        return False


    def minDays(self, bloomDay, m, k):
        n=len(bloomDay)
        if n<(m*k):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        ans=high
        while(low<=high):
            mid=(low+high)//2
            if (self.isPossible(bloomDay,mid,m,k)):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
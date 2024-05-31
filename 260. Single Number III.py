class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        l=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if(v==1):
                l.append(k)
        return l
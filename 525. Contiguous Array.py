from collections import defaultdict 
class Solution(object):
    def findMaxLength(self, nums):
        hashm = defaultdict(int)
        current = 0
        hashm[0] = -1
        maxi = 0
        for i,num in enumerate(nums):
            if num==1:
                current +=1
            else:
                current -=1
            if current in hashm:
                maxi = max(maxi, i - hashm[current])
            else :
                hashm[current] = i
        return maxi
class Solution(object):
    def largestAltitude(self, gain):
        G=[0 for i in range(0,len(gain)+1)]
        for i in range(0,len(gain)):
            G[i+1]=G[i]+gain[i]
        return max(G); 
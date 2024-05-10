class Solution(object):
    def uniquePaths(self, m, n):
        c=1
        r = m-1 if n>m else n-1
        for i in range(r): c = c*(m+n-2-i)/(i+1)
        return c
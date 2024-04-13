class Solution(object):
    def maximalRectangle(self, matrix):
        def mah(heights):
            stack=[-1]
            ans=0
            for i in range(len(heights)):
                while heights[i]<heights[stack[-1]]:
                    h=heights[stack.pop()]
                    w=i-stack[-1]-1
                    ans=max(ans,h*w)
                stack.append(i)
            return ans
        if not matrix or not matrix[0]:
            return 0
        n,m=len(matrix),len(matrix[0])
        ans=0
        height=[0]*(m+1)
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='1':
                    height[j]+=1
                else:
                    height[j]=0

            ans=max(ans,mah(height))
        return ans
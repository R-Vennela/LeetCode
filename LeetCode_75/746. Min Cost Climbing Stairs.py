class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        opt = [0] * (n+1)
       
        if n >= 0:
            opt[0] = cost[0]
        if n >= 1:
            opt[1] = cost[1]

        for i in range(2,n+1):           
            if i == n :
                c = 0
            else:
                c = cost[i]

            opt[i] = min(opt[i-1] , opt[i-2])+ c

        return opt[n]

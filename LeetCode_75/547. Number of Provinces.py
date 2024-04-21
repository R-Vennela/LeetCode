class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        # dfs will add the current node to visited
        # then go through all neighbors that also havent been visted. 
        ## A neighbor will be a node that has a connected edge aka ==1
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if j not in visited and isConnected[i][j]==1:
                    dfs(j)


        prov=0
        visited=set()
        n=len(isConnected)

        for i in range(n): #go through each node
            #if not visited, do a dfs of node and increase prov
            if i not in visited:
                dfs(i)
                prov+=1
        return prov 
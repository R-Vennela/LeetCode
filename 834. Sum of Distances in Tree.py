from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, N, edges):
        graph = defaultdict(list)
        count = [0] * N
        res = [0] * N
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs1(cur, parent) :
            count[cur] = 1
            for child in graph[cur]:
                if child != parent:
                    dfs1(child, cur)
                    count[cur] += count[child]
                    res[cur] += res[child] + count[child]
        
        def dfs2(cur, parent) :
            for child in graph[cur]:
                if child != parent:
                    res[child] = res[cur] + N - 2 * count[child]
                    dfs2(child, cur)
        
        dfs1(0, -1)
        dfs2(0, -1)
        
        return res
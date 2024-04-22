class Solution:
    def minReorder(self, n, connections) :
        
        graph = defaultdict(list)
        for a,b in connections:
            graph[a].append((b, True))
            graph[b].append((a, False))
            
        def dfs(node, visited):
            visited.add(node)
            result = 0
            for neighbour, to_reverse in graph[node]:
                if neighbour not in visited:
                    result += to_reverse
                    result += dfs(neighbour, visited)
            return result
        
        return dfs(0, set()) 
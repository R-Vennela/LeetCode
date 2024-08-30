import heapq

class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        def dijkstra():
            dist = [float('inf')] * n
            dist[source] = 0
            pq = [(0, source)]
            
            while pq:
                d, u = heapq.heappop(pq)
                if dist[u] < d:
                    continue
                for v, w in graph[u]:
                    if w == -1:  # Skip initially unknown weights
                        continue
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
            
            return dist[destination]

        # Build the graph
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # First run of Dijkstra to check the shortest path
        d = dijkstra()
        if d < target:
            return []
        
        ok = d == target
        for i in range(len(edges)):
            u, v, w = edges[i]
            if w > 0:
                continue
            if ok:
                edges[i][2] = 2 * 10**9
            else:
                edges[i][2] = 1
                graph[u].remove((v, -1))
                graph[v].remove((u, -1))
                graph[u].append((v, 1))
                graph[v].append((u, 1))
                d = dijkstra()
                if d <= target:
                    ok = True
                    edges[i][2] += target - d
                graph[u].remove((v, 1))
                graph[v].remove((u, 1))
                graph[u].append((v, edges[i][2]))
                graph[v].append((u, edges[i][2]))
        
        return edges if ok else []
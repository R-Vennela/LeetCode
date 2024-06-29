class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """

        # Topological sort
        incoming = defaultdict(set)
        outgoing = defaultdict(set)

        for edge in edges:
            incoming[edge[1]].add(edge[0])
            outgoing[edge[0]].add(edge[1])
        
        ancestors = [[] for _ in range(n)]
        cache = defaultdict(set)

        # Start with those with no incoming edges
        queue = deque()
        for i in range(n):
            if len(incoming[i]) == 0:
                queue.append(i)
                cache[i] = []


        # Progressively add all ancestors found so far
        # ALWAYS REMEMBER TO REMOVE FROM OUTGOING AND ONLY ADD TO QUEUE WHEN ZERO LEN
        while queue:

            size = len(queue)

            for i in range(size):

                node = queue.popleft()
                for out in outgoing[node]:
                    cache[out].add(node)
                    cache[out].update(cache[node])

                    incoming[out].remove(node)
                    if len(incoming[out]) == 0:
                        queue.append(out)


        index = 0
        for value in cache.values():
            ancestors[index] = sorted(list(value))
            index += 1
            
        return ancestors
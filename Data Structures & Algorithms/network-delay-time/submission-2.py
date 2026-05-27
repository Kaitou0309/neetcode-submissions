class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list) 

        for u, v, t in times: 
            edges[u].append((t, v))

        min_heap = [(0, k)] # (weight, node)
        visited = set() 
        t = 0
        while min_heap: 
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited: 
                continue 
            visited.add(n1) 

            t = max(t, w1)

            for w2, n2 in edges[n1]: 
                
                if n2 not in visited: 
                    heapq.heappush(min_heap, (w1 + w2, n2))


        return t if len(visited) == n else -1
        
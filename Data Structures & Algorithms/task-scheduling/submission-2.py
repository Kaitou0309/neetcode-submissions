class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = {}

        for t in tasks:
            counts[t] = counts.get(t, 0) + 1

        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        cooldown = deque()

        res = 0 

        while max_heap or cooldown: 

            res += 1

            while cooldown and cooldown[0][1] <= res:
                count, avail_time = cooldown.popleft()
                heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1
                if count < 0:
                    cooldown.append((count, res + n + 1))

            

        return res









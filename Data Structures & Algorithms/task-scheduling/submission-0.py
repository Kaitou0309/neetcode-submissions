class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        
        map = {} 
        
        for t in tasks: 
            
            map[t] = map.get(t, 0) + 1
            
        
        max_heap = [-n for n in map.values()]
        heapq.heapify(max_heap)
        
        count = 0
        queue = deque()
        # count + n * frequency = last time you process
        while max_heap or queue: 
            count += 1
            
            if max_heap:
                v = heapq.heappop(max_heap) + 1
                
                if v != 0:
                    queue.append((v,  count + n))
                
            while queue and count >= queue[0][1]: 
                heapq.heappush(max_heap, queue.pop()[0])
                
            
        return count
    '''
    - Keep a max-heap of tasks by their remaining count (most frequent on top).
    - At each time unit, we take the most frequent available task and run it.
    - After running a task, it goes into a cooldown queue with the time when it will be        
        available again (current time + n).
    - When a task’s cooldown finishes, we push it back into the heap so it can be scheduled 
        again.
    - If the heap is empty but some tasks are still in cooldown, we can jump the current time 
        forward to the next time when a task becomes available.
    '''
        
    # ["A","A","A","B","C"], n = 3
    # max_heap = [-1, -1]
    #              ^
    # cycle = 4
    # v = -3
    # queue = [(-2, 4), ()]
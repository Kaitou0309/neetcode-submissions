class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        hash_map = {}

        for n in nums: 
            hash_map[n] = 1 + hash_map.get(n, 0)

        min_heap = []

        for key, val in hash_map.items(): 
            heapq.heappush(min_heap, [-val, key])

        res = []

        for i in range(k): 
            res.append(heapq.heappop(min_heap)[1])

        return res
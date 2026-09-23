class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        frequency = {}

        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1

        heap = []

        for key, val in frequency.items(): 
            
            
            heapq.heappush(heap, [-val, key])

        res = []

        for i in range(k): 
            res.append(heapq.heappop(heap)[1])

        return res

        


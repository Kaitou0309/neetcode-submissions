class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        
        for i in range(k - 1):
            heapq.heappop(max_heap)
        
        return -max_heap[0]
        
            
            
        
    # [3,2,3,1,2,4,5,5,6]           i != k
    # [6, 5, 5, 4, 3, 3, 2, 2, 1], pop 6, 
    
    # [3,2,3,1,2,4,5,5,6]
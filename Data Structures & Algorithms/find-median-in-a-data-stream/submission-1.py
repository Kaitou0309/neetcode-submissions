class MedianFinder:

    def __init__(self):
       self.min_heap = []    # upper half of the list
       self.max_heap = []    # lower half of the list
       heapq.heapify(self.min_heap)
       heapq.heapify(self.max_heap)


    def addNum(self, num: int) -> None:

        if not self.max_heap or -self.max_heap[0] >= num:
            heapq.heappush(self.max_heap, -num)
        else: 
            heapq.heappush(self.min_heap, num)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -val)
        elif len(self.max_heap) < len(self.min_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        
            
        
        # print(self.min_heap)
        # print(self.max_heap)


    def findMedian(self) -> float:

        if len(self.max_heap) != len(self.min_heap):
            return float(-self.max_heap[0])
        else: 
            return (-self.max_heap[0] + self.min_heap[0]) / 2

        # print(self.min_heap)
        # print(self.max_heap)
       
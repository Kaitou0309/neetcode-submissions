class MedianFinder:

    def __init__(self):
        self.max_heap = []   # lower half of list    
        self.min_heap = []   # higher half of list


    def addNum(self, num: int) -> None:

        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        

        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            

        

    def findMedian(self) -> float:
        
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else: 
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
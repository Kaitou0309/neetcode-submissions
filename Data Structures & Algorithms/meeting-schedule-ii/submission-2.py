"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals: 
            return 0
        intervals.sort(key=lambda x: x.start)

        res = 1

        minheap = []
        heapq.heapify(minheap) 
        
        for i in range(1, len(intervals)): 
            i1 = intervals[i-1]
            i2 = intervals[i]

            heapq.heappush(minheap, i1.end)

            if minheap[0] <= i2.start: 
                heapq.heappop(minheap)
                continue

        
            
            res += 1
                

        
        return res


            




        return res


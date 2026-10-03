class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort() 

        res = [intervals[0]]

        for a, b in intervals:

            start, end = res[-1]

            if a > end:
                res.append([a,b])
                continue
            if b > end:
                res.pop()
                res.append([start, b])
        
        return res


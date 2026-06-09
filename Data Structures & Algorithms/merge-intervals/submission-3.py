class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]] 

        for s, e in intervals: 

            last_end = merged[-1][1]

            if s <= last_end: 
                merged[-1][1] = max(last_end, e)
            else: 
                merged.append([s, e])


        return merged
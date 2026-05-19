class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        l = 0
        r = len(heights) - 1
        
        vol = 0

        while l < r:
            curr_vol = (r-l) * min(heights[l], heights[r])

            if curr_vol > vol:
                vol = curr_vol

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return vol
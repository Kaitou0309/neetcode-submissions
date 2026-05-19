class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        l_wall = height[l]
        r_wall = height[r]
        ele = 0
        while l < r:             
            print(ele)
            if r_wall < l_wall:
                r -= 1
                r_wall = max(r_wall, height[r])
                ele += r_wall - height[r]
            else:
                l += 1
                l_wall = max(l_wall, height[l])
                ele += l_wall - height[l]
            
        return ele

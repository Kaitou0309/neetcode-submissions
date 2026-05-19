class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []  # idex and height

        max_area = 0 
        for i, h in enumerate(heights): 
            idx = i
            # print(stack)
            while stack and stack[-1][1] > h:
                
                l_i, l_h = stack.pop() # (3, 6), (2, 5)
                
                area = (i - l_i) * l_h # 6, 10

                # max area = max(5, 6)
                max_area = max(max_area, area)
                
                idx = l_i
                
            stack.append((idx, h))
            
        for t in stack:
            i, h = t
            area = h * (len(heights) - i)
          
            max_area = max(max_area, area)
            
        return max_area
                
                

'''
max area = 10
stack
0, 1 -> 6 = 1 * (6 - 0) = h * (len(heights) - 0)
2, 2 -> 8
5, 3 -> 3
'''
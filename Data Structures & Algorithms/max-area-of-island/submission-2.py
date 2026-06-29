class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        cols = len(grid)
        rows = len(grid[0])
        visited = set() 

        def dfs(r, c): 

            if (r < 0 or r >= rows or c < 0 or c >= cols or
             (r, c) in visited or grid[c][r] == 0):
                return 0

            visited.add((r, c)) 
            area = 1
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1) 
            area += dfs(r, c-1)
            print(area)
            return area

        res = 0
        for c in range(cols): 
            for r in range(rows): 

                if grid[c][r] == 1 and (r, c) not in visited: 
                    print(c, r)

                    res = max(res, dfs(r, c))

        return res

"""
[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]
"""
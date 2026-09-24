class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r, c): 

            if (r, c) in visited:
                return
            

            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return 

            visited.add((r,c))
            # print(visited)

            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

            
            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited: 
                    count += 1
                    dfs(i, j)
        

        return count
                

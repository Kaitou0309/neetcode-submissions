class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])

        pacific_reachable = set()
        atlantic_reachable = set() 

        def dfs(r, c, visited): 

            visited.add((r,c))

            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in direction: 
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or 
                    (nr, nc) in visited or 
                    heights[nr][nc] < heights[r][c]): 
                    continue 

                dfs(nr, nc, visited)

        for r in range(rows): 
            dfs(r, 0, pacific_reachable)
            dfs(r, cols-1, atlantic_reachable)

        for c in range(cols):
            dfs(0, c, pacific_reachable)
            dfs(rows-1, c, atlantic_reachable)

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable: 
                    res.append([r,c])

        return res
                





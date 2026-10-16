class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(queue):
            nonlocal res, fresh
            while queue and fresh > 0: 
                
                lvl_size = len(queue)

                for _ in range(lvl_size):

                    r, c = queue.popleft()

                    for dr, dc in directions: 

                        nr, nc = r + dr, c + dc

                        if 0 <= nr < rows and 0 <= nc < cols:

                            if grid[nr][nc] == 1:
                                fresh -= 1
                                grid[nr][nc] = 2
                                queue.append([nr, nc])

                res += 1

        res = 0
        fresh = 0   
        queue = deque()
        for r in range(rows):

            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append([r, c])

        bfs(queue)

        return res if fresh == 0 else -1




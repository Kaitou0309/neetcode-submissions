class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        visited = set() 

        def backtrack(r, c, index): 

            if index == len(word):
                return True

            # pruning 
            if r < 0 or r >= rows or c < 0 or c >= cols: 
                return False

            if (r, c) in visited: 
                return False 

            if board[r][c] != word[index]: 
                return False 

            visited.add((r,c))

            found = (
                backtrack(r + 1, c, index + 1) or 
                backtrack(r - 1, c, index + 1) or 
                backtrack(r, c + 1, index + 1) or 
                backtrack(r, c - 1, index + 1)
            )

            visited.remove((r,c))

            return found

                    
        

        for r in range(rows):

            for c in range(cols): 
                # backtracking 
                if backtrack(r, c, 0): 
                    return True
            


        return False
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_list = [set() for _ in range(9)]
        col_list = [set() for _ in range(9)]
        subbox_list = [set() for _ in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                key = board[i][j]
                if (key == "."):
                    continue

                if key in row_list[i]:
                    return False
                
                row_list[i].add(key)
                print("row_list ", row_list)
               
                
                if key in col_list[j]:
                    return False
                    
                col_list[j].add(key)
                print("col_list ", col_list)
                
                
                row = i // 3
                col = j // 3
                s = row * 3 + col
                
                if key in subbox_list[s]:
                    return False 
                    
                subbox_list[s].add(key)
                print("subbox_list ",subbox_list)
        
            
        return True
        

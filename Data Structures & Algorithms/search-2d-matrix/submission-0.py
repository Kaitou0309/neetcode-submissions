class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        i = 0 # start of matrix list
        j = len(matrix) - 1 # end of matrix list 
        
        while i <= j:
            k = (i + j) // 2
            h = 0
            t = len(matrix[0]) - 1
            if matrix[k][h] > target: 
                j = k - 1

            elif matrix[k][t] < target: 
                i = k + 1

            else:

                break

        while h <= t: 
                    k_1 = (h + t) // 2
                    if matrix[k][k_1] > target: 
                        t = k_1 - 1

                    elif matrix[k][k_1] < target: 
                        h = k_1 + 1

                    else: 
                        return True

        return False
        # log(mn) < log(m log(n))
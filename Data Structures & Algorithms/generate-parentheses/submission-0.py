class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(string, l, r): 

            if len(string) == 2 * n: 
                res.append(string)
                return 

            if l > r:   # pruning
                backtrack(string + ")", l, r + 1)
            
            if l < n: 
                backtrack(string + "(", l + 1, r)

        backtrack("", 0, 0)

                

        return res

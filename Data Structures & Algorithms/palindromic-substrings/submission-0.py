class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0

        def dfs(l, r): 

            nonlocal res

            if l < 0 or r >= len(s): 
                return 

            
            if s[l] != s[r]: 
                return 

            res += 1

            dfs(l-1, r+1)


        for i in range(len(s)):

            dfs(i, i)
            dfs(i, i+1)
            
        return res
            



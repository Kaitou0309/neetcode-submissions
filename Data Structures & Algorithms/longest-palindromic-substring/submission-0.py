class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        res = ""
        res_len = 0
        
        def dfs(l, r): 
            nonlocal res, res_len
            if l < 0 or r >= len(s): 
                return

            if s[l] != s[r]: 
                return 

            curr_len = r - l + 1

            if curr_len > res_len: 
                res_len = curr_len
                res = s[l:r+1]

                # print(res)

            dfs(l-1, r+1)

            

            


        for i in range(len(s)): 

            dfs(i, i)

            dfs(i, i+1)

        return res
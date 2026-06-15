class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}

        if s[0] == "0":
            return 0

        def dfs(i): 
            nonlocal memo
            if i == len(s): 
                return 1
            if i > len(s) or s[i] == "0": 
                return 0
            

            if i in memo: 
                return memo[i]

            ways = dfs(i+1)
            if i + 1 < len(s):
                if 10 <= int(s[i:i+2]) < 27: 
                    ways = ways + dfs(i+2)
                

            memo[i] = ways

            return ways


        dfs(0)
        print(memo)

        return memo[0]
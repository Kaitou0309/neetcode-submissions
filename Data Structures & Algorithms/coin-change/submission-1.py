class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0: 
            return 0

        memo = {}   # key = amt, val = num of coins
        def dfs(amt): 
            nonlocal memo
            if amt < 0: 
                return float('inf')
            if amt == 0: 
                return 0
            
            if amt in memo: 
                return memo[amt]

            best = float('inf')

            for c in coins: 
                result = dfs(amt - c)

                if result >= 0: 
                    best = min(best, result + 1)

            memo[amt] = best

            return best

        

        dfs(amount)
        if memo[amount] == float('inf'): 
            return -1
        return memo[amount]
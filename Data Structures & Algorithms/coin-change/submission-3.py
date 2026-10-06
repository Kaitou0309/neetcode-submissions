class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        memo = {}

        def dfs(curr):
            
            if curr in memo:
                return memo[curr]

            if curr == 0:
                return 0

            if curr < 0:
                return float('inf')

            best = float('inf')
            for c in coins:
                diff = curr - c
                best = min(best, dfs(diff))
            
            memo[curr] = 1 + best
            return 1 + best

        dfs(amount)

        if memo[amount] == float('inf'):
            return -1

        return memo[amount]
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(curr_val):
            if curr_val == 0:
                return 0
            if curr_val in memo:
                return memo[curr_val]
            if curr_val < 0:
                return float("inf")
            best = float("inf")
            
            for c in coins:
                candidate = 1 + dfs(curr_val - c)
                best = min(best, candidate)
                

            memo[curr_val] = best
            return best

        res = dfs(amount)
        if res == float("inf"):
            return -1
        return res

        
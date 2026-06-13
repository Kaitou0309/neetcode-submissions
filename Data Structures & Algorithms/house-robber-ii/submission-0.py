class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: 
            return nums[0]

        house_a = nums[:-1]
        house_b = nums[1:]
        def linear_rob(arr):    
            memo = {}

            def dfs(i): 

                if i >= len(arr):
                    return 0

                if i in memo: 
                    return memo[i]

                memo[i] = max(arr[i] + dfs(i+2), dfs(i+1))

                return memo[i]

            return dfs(0)

        res = max(linear_rob(house_a), linear_rob(house_b))

        return res
        
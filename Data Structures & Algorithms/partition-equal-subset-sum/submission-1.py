class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False
        
        target_sum = sum(nums) // 2

        
        memo = {}

        def dfs(i, curr_sum): 

            if curr_sum == target_sum: 
                return True
            if curr_sum > target_sum: 
                return False
            if i >= len(nums):
                return False 

            if (i, curr_sum) in memo: 
                return memo[(i, curr_sum)]
            
            take = False
            if curr_sum + nums[i] <= target_sum: 
                take = dfs(i+1, curr_sum + nums[i])

            skip = dfs(i+1, curr_sum)

            memo[(i, curr_sum)] = take or skip

            return memo[(i, curr_sum)]
        res = dfs(0, 0)
        return res


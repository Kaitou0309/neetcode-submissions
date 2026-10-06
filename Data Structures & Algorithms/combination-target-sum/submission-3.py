class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(curr, idx):

            if sum(curr) == target:
                res.append(curr.copy())
                return 

            if sum(curr) > target:
                return

            for i in range(idx, len(nums)):
                curr.append(nums[i])
                dfs(curr, i)
                curr.pop()

        dfs([], 0)
        return res
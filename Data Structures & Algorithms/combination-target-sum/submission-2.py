class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(curr, idx):

            if curr and sum(curr) == target:
                res.append(curr.copy())
                return

            if sum(curr) > target:
                return

            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i)
                curr.pop()


        backtrack([], 0)

        return res
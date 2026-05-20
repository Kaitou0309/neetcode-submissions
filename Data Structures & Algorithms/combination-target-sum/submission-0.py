class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(index, path): 

            # base case 
            if sum(path) == target: 
                res.append(path[:])
                return

            if sum(path) > target: 
                return

            # try every number from start to end
            for i in range(index, len(nums)): 
                path.append(nums[i])
                backtrack(i, path)
                path.pop() 

        backtrack(0, [])

        return res
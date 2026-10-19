class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()
        curr_list = []
        def backtrack(start):
            res.append(curr_list.copy())
            for i in range(start, len(nums)):

                if i > start and nums[i] == nums[i-1]:
                    continue
                curr_list.append(nums[i])
                backtrack(i+1)
                curr_list.pop()
        backtrack(0)
        return res
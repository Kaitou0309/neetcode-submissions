class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        visited = set()

        def backtrack(curr):

            if len(curr) == len(nums):
                res.append(curr.copy())
                return 

            for i in range(len(nums)):
                if i in visited:
                    continue

                curr.append(nums[i])
                visited.add(i)
                backtrack(curr)
                visited.remove(i)
                curr.pop()


        backtrack([])

        return res
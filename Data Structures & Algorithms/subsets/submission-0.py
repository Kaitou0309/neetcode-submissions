class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtrack(index, path): 

            # base case, of we are at last index
            if index == len(nums):
                result.append(path[:])
                return 

            # decision 1: include nums[index]
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            # decision 2: skip nums[index]
            backtrack(index + 1, path)

        backtrack(0, [])

        return result
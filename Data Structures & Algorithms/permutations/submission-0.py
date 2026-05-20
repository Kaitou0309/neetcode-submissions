class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(index, path):

            # base case 
            if index == len(nums) or len(path) == len(nums):
                res.append(path[:])
                return 

            for i in nums: 

                if i not in path: 
                    path.append(i)
                    backtrack(index + 1, path)
                    path.pop() 



        backtrack(0, [])

        return res

            

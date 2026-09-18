class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        
        prefix = 1

        for i in range(1, len(nums)): 
            res[i] = prefix * nums[i-1]
            prefix = res[i]
        # print(res)

        suffix = 1

        for i in range(len(nums) - 1, -1, -1): 

            res[i] = suffix * res[i]
            suffix = suffix * nums[i]

        return res
            
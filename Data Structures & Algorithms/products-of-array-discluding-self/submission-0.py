class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        nums_len = len(nums)
        
        prefix = [1] * nums_len
        suffix = [1] * nums_len
        res = [1] * nums_len
        
        for i in range(1, nums_len):
            
            prefix[i] = prefix[i-1] * nums[i-1] 

        print(prefix)
        
        

        for i in range(nums_len-2, -1, -1):

            suffix[i] = suffix[i+1] * nums[i+1]
        
        print(suffix)
        
        

        for i in range(nums_len):
            res[i] = prefix[i] * suffix[i]


        return res
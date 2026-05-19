class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i = 0
        j = len(nums) - 1
        
        while i <= j:
        
        
            k = (i + j) // 2
            curr = nums[k] 
            
            if curr > target: 
                j = k - 1
                
            elif curr < target:
                i = k + 1
            else:
                
                return k 
                
                
        return -1
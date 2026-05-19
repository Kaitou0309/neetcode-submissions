class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        i = 0  # left ptr
        j = len(nums) - 1 # right ptr 

        res = nums[0]
        while i < j: 

            k = (i + j) // 2

            if nums[k] > nums[i]:
                i = k + 1
                res = min(res, nums[i])
            elif nums[k] < nums[j]:
                j = k - 1
                res = min(res, nums[k])

            else: 
                i = k + 1
                res = min(res, nums[i])

        return res

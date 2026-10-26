class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False 


        memo = {}

        def recursion(i,remain):

            if remain == 0:
                return True
            
            if i == len(nums) or remain < 0:
                return False

            if (i, remain) in memo:
                return memo[(i, remain)]


            r1 = recursion(i+1, remain - nums[i])
            r2 = recursion(i+1, remain)
            memo[(i, remain)] = r1 or r2
            
            return r1 or r2
        half = sum(nums) // 2
        return recursion(0, half)
            
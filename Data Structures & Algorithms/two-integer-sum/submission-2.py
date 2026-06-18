class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for i in range(len(nums)): 
            diff = target - nums[i]
            if diff in hash_map: 
                
                n, j = hash_map[diff]
                return [j, i]
            hash_map[nums[i]] = [diff, i]

            

        return 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        


        for t in range(len(nums)):
            curr = nums[t]
            for i in range(t+1, len(nums)):

                if curr + nums[i] == target:
                    return [t, i]

            curr = nums[t]
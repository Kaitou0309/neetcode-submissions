class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        res_set = set(nums) 

        max_len = 0
        
        for i in res_set:

            if i-1 not in res_set:
            
                count = 1

                while i+count in res_set:
                    count += 1
            
                print(count)

                if max_len < count:
                    max_len = count

        return max_len
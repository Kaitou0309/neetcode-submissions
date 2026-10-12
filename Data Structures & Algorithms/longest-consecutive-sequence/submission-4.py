class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        num_set = set(nums)
        res = 0
        for n in num_set:
            
            if n-1 not in num_set:
                curr = n
                curr_len = 0
                while curr in num_set:
                    curr_len += 1
                    curr += 1

                res = max(curr_len, res)


        return res
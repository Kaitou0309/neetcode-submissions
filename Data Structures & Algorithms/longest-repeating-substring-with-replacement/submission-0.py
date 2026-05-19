class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0 
        count = {}
        res = 0
        max_freq = 0


        for right in range(len(s)): 
            # keep track of each char count
            count[s[right]] = count.get(s[right], 0) + 1

            # find max freq so far in the window
            max_freq = max(max_freq, count[s[right]])

            # check if window is valid 
            # window len - max fre char <= k
            while (right - left + 1) - max_freq > k: 
                count[s[left]] -= 1
                left += 1

            # valid window, update result
            res = max(res, right - left + 1)

        return res


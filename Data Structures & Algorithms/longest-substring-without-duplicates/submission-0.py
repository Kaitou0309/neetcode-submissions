class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sub_s = ""
        max_len = 0
        count = 0
        for c in s: 

            # check if c is in substring
            while c in sub_s: 

                count -= 1
                sub_s = sub_s[1:]
                print(sub_s)

            count += 1
            #print(count)
            sub_s += c

            if count > max_len: 
                max_len = count
        return max_len
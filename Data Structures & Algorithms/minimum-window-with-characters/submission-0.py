class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        freq_map = {}

        # use frequency map to keep track of the characters in t
        for c in t: 

            freq_map[c] = freq_map.get(c, 0) + 1

        
        ck_map = {} # window map
        
        n = len(s)
        count = 0
        i = 0
        min_len = n + 1
        
        for j, c in enumerate(s):
            
            if freq_map.get(c, 0) != 0: 
                ck_map[c] = ck_map.get(c, 0) + 1
                
            if c in freq_map and ck_map[c] == freq_map[c]:
                count += 1 # to keep track
                
            while count >= len(freq_map):
                    # update min_len
                    if min_len > j - i + 1:
                        min_len = j - i + 1
                        res = s[i:j + 1]
                        
                    # move i to next starting point
                    if freq_map.get(s[i], 0) != 0:
                        ck_map[s[i]] = ck_map[s[i]] - 1
                        
                        if ck_map[s[i]] < freq_map[s[i]]: 
                            count -= 1
                        
                    i += 1
        
        if min_len == n + 1: 
            return ""
        
        return res

# s = "ADOBECODEBANC", t = "AABC" ADOBEC
# DOBECODEBA -> ck_map = {A: 2, B: 2, C: 1} != {A: 2, B: 1, C: 1}
"""
KeyError: 'D'
       ~~~~~~~~^^^
    if freq_map[c] != 0:
Line 20 in minWindow (Solution.py)
    ret = Solution().minWindow(param_1, param_2)
Line 78 in _driver (Solution.py)
    ~~~~~~~^^
    _driver()
Line 93 in <module> (Solution.py)
"""
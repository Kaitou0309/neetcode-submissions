class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0

        visited = set() 

        i = 0
        j = 0
        while j < len(s): 
            while s[j] in visited:
                visited.remove(s[i])
                i += 1
            visited.add(s[j])
            j += 1
            res = max(res, j - i)

        return res
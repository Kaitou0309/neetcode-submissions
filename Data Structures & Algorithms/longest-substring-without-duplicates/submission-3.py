class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        visited = set()

        i = 0
        for j in range(len(s)):
            while s[j] in visited:
                visited.remove(s[i])
                i += 1

            visited.add(s[j])
            res = max(res, j - i + 1)

        return res
            
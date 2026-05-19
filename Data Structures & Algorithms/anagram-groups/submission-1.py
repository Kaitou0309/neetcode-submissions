class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dict = defaultdict(list)
        
        for i, str1 in enumerate(strs):
            count_chars = [0] * 26
            
            for c in str1:
                count_chars[ord(c) - ord('a')] += 1
            key = tuple(count_chars)
            char_dict[key].append(str1)
            
            
        return list(char_dict.values())
            

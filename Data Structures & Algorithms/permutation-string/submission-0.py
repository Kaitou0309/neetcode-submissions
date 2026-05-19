class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26 
        win_count = [0] * 26

        # fill s1_count and FIRST window of s2 

        for i in range(len(s1)): 
            s1_count[ord(s1[i]) - ord('a')] += 1
            win_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == win_count: 
            return True


        # slide window across rest of s2
        for i in range(len(s1), len(s2)):

            # add new char 
            new_char = s2[i]
            win_count[ord(new_char) - ord('a')] += 1

            # Remove old char (left side of window)
            # the old char was at index "i - len(s1)"
            old_char = s2[i - len(s1)]
            win_count[ord(old_char) - ord('a')] -= 1

            if s1_count == win_count:
                return True


        return False
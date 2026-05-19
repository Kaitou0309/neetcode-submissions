class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        j = len(s) - 1 
        i = 0
        while i <= j:
            
            if not s[i].isalnum(): 
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[j].lower() == s[i].lower():
                i += 1
                j -= 1
            else:
                return False
                
                
        return True
            
'''
A man, a plan, a canal: Panama
     ^                   ^ 

'''
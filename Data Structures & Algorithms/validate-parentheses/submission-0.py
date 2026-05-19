class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        hash_map = {
            "}" : "{",
            ")" : "(",
            "]" : "[", 
            "{" : ".",
            "(" : ".",
            "[" : "."
        }
        
        for c in s: 
            
            
            
            if stack and hash_map[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
            
            
            
        return len(stack) == 0
class Solution:
    def isValid(self, s: str) -> bool:
        
        valid_pair = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
            "[" : ".",
            "{" : ".",
            "(" : "."
        }

        stack = []

        for c in s: 

            if stack and valid_pair[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0
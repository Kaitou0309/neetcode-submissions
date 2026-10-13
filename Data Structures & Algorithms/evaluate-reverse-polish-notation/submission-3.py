class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stack = []
        hash_map = {
            "+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: int(a / b),
        }

        for t in tokens: 

            if t in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                stack.append(hash_map[t](a, b))
                # print(stack)
            else: 
                stack.append(int(t))
                # print(stack)

        return stack[-1]





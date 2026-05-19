class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        op_dict = {
            "+" : lambda a, b: int(a + b),
            "-" : lambda a, b: int(a - b),
            "*" : lambda a, b: int(a * b),
            "/" : lambda a, b: int(a / b)
        }

        for i in tokens: 
            print(stack)
            if i in op_dict: 
                b = stack.pop() 
                a = stack.pop() 
                
                result = op_dict[i](a, b)
                stack.append(result)
            else: 
                stack.append(int(i))

        return stack[-1]
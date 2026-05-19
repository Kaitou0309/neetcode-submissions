class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        print(self.minStack)

        if not self.minStack:
            self.minStack.append(val)
        else: 
            new_min = min(val, self.minStack[-1])
            self.minStack.append(new_min)

    def pop(self) -> None:
        
        popped_val = self.stack.pop()
        
        self.minStack.pop()
        # print(self.minStack)

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        

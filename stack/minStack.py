class MinStack: 

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        return self.stack.append(val)
        

    def pop(self) -> None:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        
obj = MinStack()

# Push values onto the stack
obj.push(5)
obj.push(3)
obj.push(7)

# Get the top element
print("Top element:", obj.top())  # Expected output: 7

# Get the minimum element
print("Minimum element:", obj.getMin())  # Expected output: 3

# Pop an element
obj.pop()

# Get the top element after pop
print("Top element after pop:", obj.top())  # Expected output: 3

# Get the minimum element after pop
print("Minimum element after pop:", obj.getMin())  # Expected output: 3

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
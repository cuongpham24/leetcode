class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop()
    
    def __repr__(self) -> str:
        return str(self.stack)
    
    def __str__(self):
        return str(self.stack)

if __name__ == "__main__":
    stack = Stack()
    # Add 1 and 3 to a stack
    stack.push(1)
    stack.push(3)
    print("Stack =", stack)
    val = stack.pop()
    print("Popped value =", val)
    print("Stack =", stack)
    
class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, vale):
        self.items.append(vale)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("Pass" if (stack.size() == 5) else "Fail")

stack.push(5)
print("Pass" if (stack.size() == 5) else "Fail")

print("Pass" if (stack.pop() == 5) else "Fail")
print("Pass" if (stack.pop() == 4) else "Fail")

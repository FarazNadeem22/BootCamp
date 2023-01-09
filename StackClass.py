
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_nodes = 0

    def push(self, value):
        new_node = Node(value)

        # Check the head is not None
        if self.head is not None:
            new_node.next = self.head

        # Make new_node the head node
        self.head = new_node
        self.num_nodes += 1

    def pop(self):
        # Check if stack is empty
        if self.head == None:
            return None
        else:
            pop_node = self.head.value
            self.head = self.head.next
            self.num_nodes -= 1
            return pop_node


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("Pass" if (stack.num_nodes == 5) else "Fail")

stack.push(5)

print("Pass" if (stack.num_nodes == 5) else "Fail")
print("Pass" if (stack.pop() == 5) else "Fail")
print("Pass" if (stack.pop() == 4) else "Fail")

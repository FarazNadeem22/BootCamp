"""Double linked list"""


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)

        # If Empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print(f"Head node created {self.head.value}")
        else:
            # If not empty
            new_node.prev = self.tail  # self.tail points to the last node
            self.tail.next = new_node
            self.tail = new_node
            print(
                f"Appended to the last position in the DoublyLinkedList {self.tail.value}")

    def prettyPrint(self):
        ptr = self.head
        while ptr and ptr.next:
            print(str(ptr.value)+"->", end="")
            ptr = ptr.next
        print(ptr.value)


dllist = DoublyLinkedList()
dllist.append("1")
dllist.append("2")
dllist.append("3")
dllist.append("4")
dllist.prettyPrint()

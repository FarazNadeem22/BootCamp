"""Linked list"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        # If the linked list is empty
        if self.head is None:
            # Empty list set head pointer equal to value
            self.head = new_node
            print(f"Head node create {self.head.value}")
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next

            # Now place new_node at the end
            ptr.next = new_node
            print(
                f"Node with value {new_node.value} appended to the linked list")

    def prettyPrint(self):
        ptr = self.head
        while ptr and ptr.next:
            print(str(ptr.value)+"->", end="")
            ptr = ptr.next
        print(ptr.value)


llist = LinkedList()
llist.append("1")
llist.append("2")
llist.append("3")
llist.prettyPrint()

class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, node) -> None:
        self.head = node
        self.tail = self.head
        self.length = 1

    def insertEnd(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.length += 1

    def remove(self, index):
        assert index < self.length + 1, "Out of index"

        i = 0
        curr = self.head
        # Loop to the node before index
        while i < index - 1:
            curr = curr.next
            i += 1

        # Remove node at index
        if index == 0:
            self.head = curr.next
        else:
            curr.next = curr.next.next

        if curr.next == None:
            self.tail = curr

        self.length -= 1
        
    def print(self):
        result = []
        curr = self.head
        while curr:
            result.append(str(curr.value))
            curr = curr.next
        print(' -> '.join(result))

if __name__ == "__main__":
    node = Node(0)
    # Initialize linkedlist
    linkedList = LinkedList(node)
    linkedList.print()
    # Add node
    linkedList.insertEnd(1)
    linkedList.insertEnd(2)
    linkedList.insertEnd(3)
    linkedList.insertEnd(4)
    linkedList.print()
    # Remove node
    linkedList.remove(0)
    linkedList.print()
    linkedList.remove(1)
    linkedList.print()
    linkedList.remove(2)
    linkedList.print()

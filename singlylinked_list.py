#singly linked list implementation in python
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()
# Example usage
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.print_list() ''' # Output: 1 2 3
#isert at the end of the linked list
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

# Example usage
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.print_list()  # Output: 1 2 3
#40 insert at the beginning of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()
# Example usage
sll = SinglyLinkedList()

sll.append(1)
sll.append(2)   
sll.append(3)
sll.prepend(0)
sll.print_list()'''  # Output: 0 1 2 3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()
# Example usage
sll = SinglyLinkedList()
sll.append(1)

sll.append(2)
sll.append(3)
sll.prepend(0)
sll.print_list()  # Output: 0 1 2 3

def insertLast(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    last_node = self.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = new_node

def insertFirst(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

    if __name__ == "__main__":
    sll = SinglyLinkedList()
    n = int(input("Enter the number of elements to insert: "))
    for _ in range(n):
        data = int(input("Enter the element to insert: "))
        sll.insertLast(data)
    print("Linked List after inserting elements at the end:")
    sll.print_list()
    m = int(input("Enter the number of elements to insert at the beginning: "))
    for _ in range(m):
        data = int(input("Enter the element to insert at the beginning: "))
        sll.insertFirst(data)
    print("Linked List after inserting elements at the beginning:")
    sll.print_list()
    




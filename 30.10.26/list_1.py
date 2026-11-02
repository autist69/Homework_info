"""
Попросил помощь у ИИ в создании односвязного списка.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def search(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next   
        return False

A = SinglyLinkedList()
for i in [5, 9, 13, 4]:
    A.append(i)
        
print(A.search(9))
print(A.search(10))

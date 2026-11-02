class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data, place):
        if place == 1 and self.head is not None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        elif place == 1 and self.head is None:
            self.head = Node(data)
        elif place > 1 and self.head is None:
            print("Number is out of the list.")
        else:
            last_node = self.head
            n = 1
            while last_node.next is not None and n < place - 1:
                last_node = last_node.next
                n += 1
            if n == place - 1:
                new_node = Node(data)
                new_node.next = last_node.next
                last_node.next = new_node
            else:
                print("Value out of the list.")
                return

    def value_delete(self, value):
        if self.head is None:
            print("List is empty.")
            return
        elif self.head.data == value:
            self.head = self.head.next
        else:
            last_node = self.head
            while last_node is not None:
                if last_node.next is not None and last_node.next.data == value:
                    break
                last_node = last_node.next

            if last_node == None:
                print("Value is not in the list.")
                return
            else:
                last_node.next = last_node.next.next

    def print_list(self):
        if self.head is None: 
            print("List has no elements") 
            return
        else:
            last_node = self.head
            while last_node is not None:
                print(last_node.data)
                last_node = last_node.next

A = SinglyLinkedList()
res = SinglyLinkedList()
numbers = [5, 9, 13, 4, 85, 39]

for i in range(6):
    A.append(numbers[i], i + 1)
    res.append(numbers[i], i + 1)

res.append(45, 4)
res.value_delete(9)
        
n = int(input())
last_node = res.head
for i in range (1, n):
    value = last_node.data
    res.value_delete(value)
    last_node = last_node.next

A.print_list()
res.print_list()

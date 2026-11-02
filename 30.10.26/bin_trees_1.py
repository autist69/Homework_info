class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def compare_trees(first, second):
    if first is None and second is None:
        return True
    elif first is None or second is None:
        return False
    elif (first.key == second.key and compare_trees(first.left, second.left)
          and compare_trees(first.right, second.right)):
        return True
    return False

x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(8)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

y = Node(15)
y.left = Node(10)
y.right = Node(20)
y.left.left = Node(8)
y.left.right = Node(12)
y.right.left = Node(16)
y.right.right = Node(25)

z = Node(15)
z.left = Node(10)
z.right = Node(20)
z.left.left = Node(8)
z.left.right = Node(12)
z.right.left = Node(16)
z.right.right = None

print(compare_trees(x, y))
print(compare_trees(x, z))
print(compare_trees(y, z))

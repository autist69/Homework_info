class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def swap_tree(tree):
    if tree.right is None and tree.left is None:
        return
    else:
        l = tree.left
        r = tree.right
        tree.left = r
        tree.right = l
        swap_tree(tree.left)
        swap_tree(tree.right)

x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(8)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

print(x.key)
print(x.left.key, x.right.key)
print(x.left.left.key, x.left.right.key, x.right.left.key, x.right.right.key)

swap_tree(x)

print(x.key)
print(x.left.key, x.right.key)
print(x.left.left.key, x.left.right.key, x.right.left.key, x.right.right.key)

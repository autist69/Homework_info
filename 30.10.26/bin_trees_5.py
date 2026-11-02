class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def find_node(node, tree):
    if tree is None:
        return False
    elif node is tree:
        return True
    else:
        return find_node(node, tree.left) or find_node(node, tree.right)

def find_next_node(node, tree, ancestors):
    l = tree.left
    r = tree.right
    if find_node(node, l):
        ancestors.append(tree.key)
        find_next_node(node, l, ancestors)
    elif find_node(node, r):
        ancestors.append(tree.key)
        find_next_node(node, r, ancestors)
    return

def find_ancestors(node, tree):
    ancestors = []
    if tree is node:
        print("Don't have any ancestors.")
    else:
        find_next_node(node, tree, ancestors)
    return ancestors

x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(8)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

print(find_ancestors(x.left.right, x))

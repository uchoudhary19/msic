class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

import random

root = None

values  = []
v = 0
val_length = 10

while v < val_length:
    n = random.randint(0, 100)
    values.append(n)
    v += 1

print(values)

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.val:
        root.left = insert(root.left, value)
    if value > root.val:
        root.right = insert(root.right, value)
    return root

for val in values:
    root = insert(root, val)

def search_bst(root, value):
    if root is None:
        print('No Tree to Search')
        return False
    if root.val == value:
        print(f"found the node value {root.val}")
        return True
    elif value < root.val:
        return search_bst(root.left, value)
    else:
        return search_bst(root.right, value)

search_bst(root, values[3])

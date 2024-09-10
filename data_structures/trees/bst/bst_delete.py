class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def delete_node(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)
    return root

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Test
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

root = delete_node(root, 50)
inorder(root)  # Output: 20 30 40 60 70 80

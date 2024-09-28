class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.val, end=" ")
        inorder_recursive(root.right)

def preorder_recursive(root):
    if root:
        print(root.val, end=" ")
        preorder_recursive(root.left)
        preorder_recursive(root.right)

def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.val, end=" ")

# Test
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal (Recursive):")
inorder_recursive(root)  # Output: 4 2 5 1 3

print("\nPreorder traversal (Recursive):")
preorder_recursive(root)  # Output: 1 2 4 5 3

print("\nPostorder traversal (Recursive):")
postorder_recursive(root)  # Output: 4 5 2 3 1

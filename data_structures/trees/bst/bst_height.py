class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bst_height(root):
    if root is None:
        return -1
    left_height = bst_height(root.left)
    right_height = bst_height(root.right)
    return 1 + max(left_height, right_height)

# Test
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of BST:", bst_height(root))  # Output: 2

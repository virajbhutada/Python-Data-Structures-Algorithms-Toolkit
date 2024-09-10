class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def inorder(root):
    return inorder(root.left) + [root.value] + inorder(root.right) if root else []

def preorder(root):
    return [root.value] + preorder(root.left) + preorder(root.right) if root else []

def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.value] if root else []

# Test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder:", inorder(root))  # Output: [4, 2, 5, 1, 3]
print("Preorder:", preorder(root))  # Output: [1, 2, 4, 5, 3]
print("Postorder:", postorder(root))  # Output: [4, 5, 2, 3, 1]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Build example tree manually
def create_tree():
    root = Node(10)

    root.left = Node(20)
    root.right = Node(30)

    root.left.left = Node(40)
    root.left.right = Node(50)

    return root


# Inorder Traversal (LNR)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Example usage
root = create_tree()

print("Inorder Traversal:")
inorder(root)
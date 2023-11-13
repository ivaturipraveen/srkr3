class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def flatten_bst_to_linked_list(root, prev=None):
    if not root:
        return None

    flatten_bst_to_linked_list(root.left, prev)
    
    if prev:
        root.left = None
        prev.right = root
    else:
        head = root

    flatten_bst_to_linked_list(root.right, root)

# Example usage:
# Construct a BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# Convert BST to linked list
flatten_bst_to_linked_list(root)

# Print the linked list
current = root
while current:
    print(current.value, end=' ')
    current = current.right

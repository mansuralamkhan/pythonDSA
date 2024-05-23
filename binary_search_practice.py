class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def inorder_traversal(node):

    if node is not None:
        inorder_traversal(node.left)
        print(node.val)
        inorder_traversal(node.right)


print("Inorder Traversal")
inorder_traversal(root)
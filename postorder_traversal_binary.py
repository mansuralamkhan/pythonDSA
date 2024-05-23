class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def postorder_traversal(root):
    if root:

        postorder_traversal(root.left)

        postorder_traversal(root.right)

        print(root.val, end=" ")


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Postordeer traversal: ")
postorder_traversal(root)



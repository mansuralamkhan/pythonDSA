class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self):
        self._preorder_traversal_helper(self.root)

    
    def _preorder_traversal_helper(self, root):
        if root:
            print(root.val, end=" ")
            self._preorder_traversal_helper(root.left)
            self._preorder_traversal_helper(root.right)


binary_tree = BinaryTree()

binary_tree.root = TreeNode(1)
binary_tree.root.left = TreeNode(2)
binary_tree.root.right = TreeNode(3)
binary_tree.root.left.left = TreeNode(4)
binary_tree.root.left.right = TreeNode(5)

print("preorder traversal")
binary_tree.preorder_traversal()
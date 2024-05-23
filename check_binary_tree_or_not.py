class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def is_bst(self):
        return self._is_bst_helper(self.root, float('-inf'), float('inf'))
    
    def _is_bst_helper(self, node, min_val, max_val):
        if node is None:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (self._is_bst_helper(node.left, min_val, node.val)) and self._is_bst_helper(node.right, node.val, max_val)
    


    
binary_tree = BinaryTree()

binary_tree.root = TreeNode(4)
binary_tree.root.left = TreeNode(9)
binary_tree.root.right = TreeNode(6)
binary_tree.root.left.left = TreeNode(1)
binary_tree.root.left.right = TreeNode(3)
binary_tree.root.right.left = TreeNode(5)
binary_tree.root.right.right = TreeNode(7)

if binary_tree.is_bst():
    print("The binary tree is a Binary search tree")
else:
    print("The binary tree is not a binary search treee")
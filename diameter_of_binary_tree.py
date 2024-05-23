class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def tree_height(root):
    if root is None:
        return 0
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    return max(left_height, right_height) +1 

def diameter_of_binary_tree(root):
    if root is None:
        return 0
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    left_diameter = diameter_of_binary_tree(root.left)
    right_diameter = diameter_of_binary_tree(root.right)

    return max(left_height + right_height + 1, max(left_diameter, right_diameter))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

diameter = diameter_of_binary_tree(root)
print("Diameter of the binary tree:", diameter)
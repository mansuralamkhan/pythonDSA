class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_height(root):
    if root is None:
        return 0
    

    left_height = find_height(root.left)
    right_height = find_height(root.right)

    return max(left_height, right_height) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

height = find_height(root)
print("height of the binary tree", height)
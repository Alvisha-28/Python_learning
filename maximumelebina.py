#design an algorithm to find the minimum element in a binary tree efficiently
'''class TreeNode:
    def __init__(self, quantity):
        self.quantity = quantity
        self.left = None
        self.right = None
def find_min_quantity(root):
    if root is None:
        return float('inf')  # Return positive infinity for null nodes
    left_min = find_min_quantity(root.left)  # Find min in left subtree
    right_min = find_min_quantity(root.right)  # Find min in right subtree
    return min(root.quantity, left_min, right_min)  # Return the minimum of current node and its subtrees
# Example usage:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
min_quantity = find_min_quantity(root)
print("Minimum item quantity in the binary tree:", min_quantity)'''  # Output: 3
class TreeNode:
    def __init__(self, quantity):
        self.quantity = quantity
        self.left = None
        self.right = None
        def insert(root, quantity):
            if root is None:
                return TreeNode(quantity)
            if quantity < root.quantity:
                root.left = insert(root.left, quantity)
            else:
                root.right = insert(root.right, quantity)
            return root
def find_min_quantity(root):
    if root is None:
        return float('inf')  # Return positive infinity for null nodes
    left_min = find_min_quantity(root.left)  # Find min in left subtree
    right_min = find_min_quantity(root.right)  # Find min in right subtree
    return min(root.quantity, left_min, right_min)  # Return the minimum of current node and its subtrees
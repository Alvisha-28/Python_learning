# #write a program to find maximum item quantity stored in binary tree,where each node contains item quantity and the tree is not necessarily a binary search tree
# '''class TreeNode:
#     def __init__(self, quantity):
#         self.quantity = quantity
#         self.left = None
#         self.right = None
# def find_max_quantity(root):
#     if root is None:
#         return float('-inf')  # Return negative infinity for null nodes
#     left_max = find_max_quantity(root.left)  # Find max in left subtree
#     right_max = find_max_quantity(root.right)  # Find max in right subtree
#     return max(root.quantity, left_max, right_max)  # Return the maximum of current node and its subtrees
# # Example usage:
# root = TreeNode(10)
# root.left = TreeNode(20)
# root.right = TreeNode(5)
# root.left.left = TreeNode(15)
# root.left.right = TreeNode(25)
# max_quantity = find_max_quantity(root)
# print("Maximum item quantity in the binary tree:", max_quantity)''' # Output: 25
# #write a program to find the maximum quantity
# # stored in binary tree where each node contains an integer value representing the quantity items in that section of the warehouse and also pls create a tree
# #how to find second largest quantity in the binary tree 
# class TreeNode:
#     def __init__(self, quantity):
#         self.quantity = quantity
#         self.left = None
#         self.right = None
# def find_max_quantity(root):
#     if root is None:
#         return float('-inf')  # Return negative infinity for null nodes
#     left_max = find_max_quantity(root.left)  # Find max in left subtree
#     right_max = find_max_quantity(root.right)  # Find max in right subtree
#     return max(root.quantity, left_max, right_max)  # Return the maximum of current node and its subtrees
# def find_second_largest(root):
#     if root is None:
#         return float('-inf')  # Return negative infinity for null nodes
#     max_quantity = find_max_quantity(root)  # Find the maximum quantity in the tree
#     second_largest = float('-inf')  # Initialize second largest to negative infinity
#     def helper(node):
#         nonlocal second_largest
#         if node is None:
#             return
#         if node.quantity != max_quantity and node.quantity > second_largest:
#             second_largest = node.quantity  # Update second largest if current node's quantity is less than max and greater than current second largest
#         helper(node.left)  # Traverse left subtree
#         helper(node.right)  # Traverse right subtree
#     helper(root)
#     return second_largest
# # Example usage:
# root = TreeNode(10)
# root.left = TreeNode(20)
# root.right = TreeNode(5)
# root.left.left = TreeNode(15)
# root.left.right = TreeNode(25)
# max_quantity = find_max_quantity(root)
# second_largest_quantity = find_second_largest(root)
# print("Maximum item quantity in the binary tree:", max_quantity)  # Output: 25
# print("Second largest item quantity in the binary tree:", second_largest_quantity)  # Output





class TreeNode:
    def __init__(self, quantity):
        self.quantity = quantity
        self.left = None
        self.right = None
def find_max_quantity(root):
    if root is None:
        return float('-inf')  # Return negative infinity for null nodes
    left_max = find_max_quantity(root.left)  # Find max in left subtree
    right_max = find_max_quantity(root.right)  # Find max in right subtree
    return max(root.quantity, left_max, right_max)  # Return the maximum of current node and its subtrees
def find_second_largest(root):
    if root is None:
        return float('-inf')  # Return negative infinity for null nodes
    max_quantity = find_max_quantity(root)  # Find the maximum quantity in the tree
    second_largest = float('-inf')  # Initialize second largest to negative infinity
    def helper(node):
        nonlocal second_largest
        if node is None:
            return
        if node.quantity != max_quantity and node.quantity > second_largest:
            second_largest = node.quantity  # Update second largest if current node's quantity is less than max and greater than current second largest
        helper(node.left)  # Traverse left subtree
        helper(node.right)  # Traverse right subtree
    helper(root)
    return second_largest
# Example usage:
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(5)
root.left.left = TreeNode(15)
root.left.right = TreeNode(25)
max_quantity = find_max_quantity(root)
second_largest_quantity = find_second_largest(root)
print("Maximum item quantity in the binary tree:", max_quantity)  # Output: 25
print("Second largest item quantity in the binary tree:", second_largest_quantity)  # Output








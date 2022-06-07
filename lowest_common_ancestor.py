# Question: Given two nodes in a binary tree, write a function to find the lowest common
# ancestor

# Clarifications: What is meant by lowest? Lowest vertically but highest level

# Solution: Recursive, if child nodes both return a non-null value, then that is lowest common. If only null is returned,
#  then p and q are not children on that side. Return the valid left or right so it can be sent up the ladder

# Complexity: O(n) time, O(height) space

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    if root in [None, p, q]:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right

root = TreeNode(3)
root.right = TreeNode(1)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

#                       3
#               5               1
#           6       2       0       8
p = root.left.left
q = root.right
print(lowestCommonAncestor(root, p, q).val)

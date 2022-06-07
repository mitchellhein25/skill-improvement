# Question: Given a tree, write a function to find the length of the longest branch of nodes
# in increasing consecutive order.

# Clarifications: Ensure you understand what is needed.

# Solution: Recursive, calculate left and right. If next value is current + 1, then call recursive and add 1, else
#   just call the recursive. return the max of left and right

# Complexity:

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def long_branch(root: 'Node') -> int:

    if root == None:
        return 0

    left, right = 1, 1
    if root.left:
        if root.left.val == root.val + 1:
            left = long_branch(root.left) + 1
        else:
            left = long_branch(root.left)
    if root.right:
        if root.right.val == root.val + 1:
            right = long_branch(root.right) + 1
        else:
            right = long_branch(root.right)

    return max(left, right)


#             1
#      2             7
# -2       4     6       8
#                            9

# returns: 3

root = Node(1)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(-2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
root.right.right.right = Node(9)

print(long_branch(root))
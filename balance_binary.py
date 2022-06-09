# Question: Given a binary tree, write a function to determine whether the tree is balanced.

# Clarifications: Balanced means no subtree has a height differential of its left and right subtrees of more than 1

# Solution: Determine height difference recursively, if ever graeter than 1, return -1. Then always return -1, if -1 at
#   end, return False

# Complexity: O(n) time , O(h) space because stores on call stack until it reaches a leaf

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def balanced_binary(node: 'Node') -> bool:

    return False if diff_height(node) == -1 else True

def diff_height(node: 'Node') -> int:

    if node == None:
        return 0

    hr = diff_height(node.right)
    hl = diff_height(node.left)

    if hr == -1 or hl == -1:
        return -1

    if abs(hr - hl) > 1:
        return -1

    return hr + 1 if hr > hl else hl + 1

#                       1
#               2               3
#           4       5
#       6


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)

print(balanced_binary(root))
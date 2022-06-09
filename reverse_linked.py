# Question: Given a linked list, write a function that prints the nodes of the list in reverse
# order.

# Clarifications: Make sure that all we want to do is print. What kind of values in array, print on separate line,
#  size of the array?

# Solution:
# Option 1: Reverse the linked list, then iterate through
# Option 2: Recursive to bottom and then print

# Complexity:
# Option 1: O(n^2) time, O(1) space
# Option 2: O(n) time, O(n) space (call stack)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# 1 -> 2 -> 3

def reverse_list(node: 'Node'):

    if node == None:
        return

    reverse_list(node.next)

    print(node.val)

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)

# 1 -> 2 -> 3

reverse_list(root)
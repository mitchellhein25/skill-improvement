# Question: Given a tree, write a function to convert it into a circular doubly linked list from
#  left to right by only modifying the existing pointers.

# Clarifications: What to return, verify some proper inputs

# Solution: Recursive, get the left and right list recursively, then combine those together with the root in the middle

# Complexity: O(n) time, O(log n) space)

class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#               1
#       2               3
#   4       5       6       7

# tree_to_list(1)
# leftList = <- 4 <-> 2 <-> 5 ->
# rightList = <- 6 <-> 3 <-> 7 ->
# <- 4 <-> 2 <-> 5 <-> 1 ->

def tree_to_list(root: 'Node') -> 'Node':
    if root == None:
        return root

    leftList = tree_to_list(root.left)
    rightList = tree_to_list(root.right)

    root.left = root
    root.right = root

    root = combine(leftList, root)
    root = combine(root, rightList)

    return root

def combine(a: 'Node', b: 'Node') -> 'Node':
    if a == None:
        return b

    if b == None:
        return a

    aEnd = a.left
    bEnd = b.left

    a.left = bEnd
    bEnd.right = a
    aEnd.right = b
    b.left = aEnd

    return a



#               1
#       2               3
#   4       5       6       7

# result: <- 4 <-> 2 <-> 5 <-> 1 <-> 6 <-> 3 <-> 7 ->
# current:                   4 <- 2 <- 1 -> 3

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

new_root = tree_to_list(root)
print(new_root.val)
new_root = new_root.right
while new_root != root:
    print(new_root.val)
    new_root = new_root.right
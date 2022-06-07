# Question: Implement a binary tree with a method getRandomNode() that returns a random node.

# Clarifications: Implement the entire data structure or just write a method for an already implemented?

# Solution:
# Brute Force: Create an array with all elements and return a random value
# Optimal: Store children on the Node object, then have a recursive function. Call random number based on root
#  children, then pass to recursive. Base case: count == get_children, return curr.val. If less, go left, else go right.

# Complexity:
# Brute Force: O(n) time and O(n) space
# Optimal: O(log n) time and O(1) space

from random import randint

class Node:

    def __init__(self, val  ):
        self.val = val
        self.children = 0
        self.left = None
        self.right = None

    def add_node(self):
        pass

    def remove_node(self):
        pass

    # Helper Function to return a random node
    def randomNodeUtil(self, curr, count):
        if count == self.get_children(curr.left):
            return curr.val

        if count < self.get_children(curr.left):
            return self.randomNodeUtil(curr.left, count)

        return self.randomNodeUtil(curr.right,
                              count - self.get_children(curr.left) - 1)

    # Returns Random node
    def randomNode(self, root):
        if root == None:
            raise Exception("Root of tree is null.")

        count = randint(0, root.children)
        return self.randomNodeUtil(root, count)

    def get_children(self, n):
        if n == None:
            return 0
        else:
            return n.children + 1

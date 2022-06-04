# Question: Implement N > 0 stacks using a single array to store all stack data (you may
#   use auxiliary arrays in your stack object, but all of the objects in all of the stacks must
#   be in the same array). No stack should be full unless the entire array is full.

# Clarifications: What to do when popping from empty or pushing to full?

# Solution: Initialize an array of capacity * num. Then array of pointers. put and pop adjust pointers

# Complexity:


class Stacks:

    def __init__(self, num, capacity):
        self.stacks_array = [0 for x in range(capacity * num)]
        self.pointers = [x for x in range(capacity * num) if x % capacity == 0]

    def print_pointers(self):
        print(self.pointers)

    def put(self, num, val):
        pointer = self.pointers[num]
        self.stacks_array[pointer] = val
        self.pointers[num] += 1

    def pop(self, num):
        pointer = self.pointers[num] - 1
        val = self.stacks_array[pointer]
        self.stacks_array[pointer] = 0
        self.pointers[num] -= 1
        return val

stacks = Stacks(3, 10)
stacks.print_pointers()
stacks.put(0, 10)
stacks.put(2, 11)
print(stacks.pop(0))
print(stacks.pop(2))
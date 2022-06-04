# Question: Given 2 sorted arrays, A and B, where A is long enough to hold the contents of
# A and B, write a function to copy the contents of B into A without using any buffer or
# additional memory

# Clarification: Does A just have empty values at end to make it large enough?

# Solution: Insert next smallest into a, then pop the last element, or insert largest from back to front of a.

# Complexity: O(n + m)

def merge_arrays(a, b) -> list[int]:

    b_pointer = 0
    for x in range(len(a)):

        if b[b_pointer] <= a[x] or a[x] == 0:
            a.insert(x, b[b_pointer])
            b_pointer += 1
            a.pop(len(a) - 1)

        if b_pointer == len(b):
            break
    return a


a = [1,3,5,0,0,0]
b = [2,4,6]
print(merge_arrays(a, b))
a = [1,2,3,0,0,0]
b = [4,5,6]
print(merge_arrays(a, b))
a = [1,2,3,0,0,0]
b = [1,1,6]
print(merge_arrays(a, b))
a = [4,5,6,0,0,0]
b = [1,2,3]
print(merge_arrays(a, b))
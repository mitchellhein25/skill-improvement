# Question: Given an n x m array where all rows and columns are in sorted order, write a
#  function to determine whether the array contains an element x.

# Clarifying Questions: Clarify the way the sorting works. Are all columns same size and rows same size?

# Solution: Start at top right, if greater, then increment row, if smaller, then decrement column

# Complexity: O (n + m) time, O(1) space

def matrix_search(matrix, element) -> bool:

    x = 0
    y = len(matrix[0]) - 1

    while x < len(matrix) and y >= 0:

        if matrix[x][y] == element:
            return True

        elif matrix[x][y] < element:
            x += 1

        else:
            y -= 1

    return False

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
for ea in matrix:
    print(ea)
print(matrix_search(matrix, 13))
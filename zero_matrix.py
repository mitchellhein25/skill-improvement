# Question: Given a boolean matrix, update it so that if any cell is true, all the cells in that
# row and column are true.

# Clarifying questions: In place or generating a new matrix, is it all 1 operation, so the falses don't change

# Solution: First get if first row or col contains a True. Then Set first row and columns to true if a
# true value is found, then set all values at the end

# Time Complexity: O(n^2), O(1) space

def zero_matrix(matrix) -> list[list[bool]]:
    col_len, row_len = len(matrix), len(matrix[0])
    col_zero, row_zero = False, False

    # Get first row and column values
    for x in matrix:
        col_zero |= x[0]
    for x in matrix[0]:
        row_zero |= x

    # Set first rows based on if a True is found anywhere
    for x in range(1, col_len):
        for y in range(1, row_len):
            matrix[x][0] |= matrix[x][y]
            matrix[0][y] |= matrix[x][y]

    # Set all values based on first row
    for x in range(1, col_len):
        for y in range(1, row_len):
            matrix[x][y] |= matrix[0][y] or matrix[x][0]

    # Set remaining first row and column values
    if col_zero:
        for y in range(0, col_len):
            matrix[y][0] = True
    if row_zero:
        for y in range(0, row_len):
            matrix[0][y] = True

    return matrix

print("Test 1")
for row in [[True,False,False], [False,False,False], [False,False,False]]:
    print(row)
for row in zero_matrix([[True,False,False], [False,False,False], [False,False,False]]):
    print(row)


print("Test 2")
for row in [[True,False,False], [False,False,False], [False,True,False]]:
    print(row)
for row in zero_matrix([[True,False,False], [False,False,False], [False,True,False]]):
    print(row)
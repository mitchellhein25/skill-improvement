# Question: Given a 2D array of 1s and 0s, find the largest square subarray of all 1s.

# Clarifications: Does it have to be solid throughout? Return length of longest side, or number of items, or actual
#  matrix?

# Solution: Bottom-up memoization. Keep track of bottom left corners in separate matrix. If the left, top-left, and
# top-right have a value, take the min and add one

# Time Complexity:  O(n*m) time and space

def square_submatrix(matrix) -> int:
    if len(matrix) == 0:
        return 0
    if len(matrix[0]) == 0:
        return 0

    dyn_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    result = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):

            if matrix[x][y] == 1:

                if x == 0 or y == 0:
                    dyn_matrix[x][y] = 1
                    result = max(result, 1)

                elif dyn_matrix[x - 1][y] != 0 and dyn_matrix[x][y - 1] != 0:
                    dyn_matrix[x][y] = min(dyn_matrix[x][y - 1], dyn_matrix[x - 1][y], dyn_matrix[x - 1][y - 1]) + 1
                    result = max(result, dyn_matrix[x][y])

                else:
                    dyn_matrix[x][y] = 1
                    result = max(result, 1)
    # print()
    # for row in dyn_matrix:
    #     print(row)

    return result

for row in [[1,1,1,0],[1,1,1,1],[1,1,0,0]]:
    print(row)

print()
print(square_submatrix([[1,1,1,0],[1,1,1,1],[1,1,0,0]]))
print()
for row in [[0,1,1,1],[1,0,1,1],[1,1,1,1]]:
    print(row)

print()
print(square_submatrix([[0,1,1,1],[1,0,1,1],[1,1,1,1]]))
print(square_submatrix([[0,1,1,1],[1,0,1,1],[1,1,1,1]]))
print(square_submatrix([]))
print(square_submatrix([[0]]))
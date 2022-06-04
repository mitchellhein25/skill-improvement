# Question: Given a matrix, find the path from top left to bottom right with the greatest
# product by moving only down and right.

# Solution: Keep track of most negative and most positive solutions in separate matrices

# Time complexity: O(n) Space: O(2n)

def matrix_product(matrix) -> int:
    length = len(matrix)
    maxes = [[0 for x in range(length)] for x in range(length)]
    mins = [[0 for x in range(length)] for x in range(length)]

    for x in range(length):
        for y in range(length):
            if x == 0 and y == 0:
                maxes[0][0], mins[0][0] = matrix[0][0], matrix[0][0]

            elif x == 0:
                new_val = maxes[x][y - 1] * matrix[x][y]
                maxes[x][y], mins[x][y] = new_val, new_val

            elif y == 0:
                new_val = maxes[x - 1][y] * matrix[x][y]
                maxes[x][y], mins[x][y] = new_val, new_val

            else:
                max_t = maxes[x - 1][y] * matrix[x][y]
                max_l = maxes[x][y - 1] * matrix[x][y]
                min_t = mins[x - 1][y]  * matrix[x][y]
                min_l = mins[x][y - 1]  * matrix[x][y]
                maxes[x][y] = max(max_t, max_l, min_t, min_l)
                mins[x][y] = min(max_t, max_l, min_t, min_l)

    # for row in maxes:
    #     print(row)
    # for row in mins:
    #     print(row)

    return maxes[length - 1][length - 1]

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix_product(matrix)) # 2016

matrix = [[-1,2,3], [4,5,-6], [7,8,9]]
print(matrix_product(matrix)) # 1080
# Given a list of items with values and weights, as well as a max weight, find the
# maximum value you can generate from items where the sum of the weights is less than
# the max.

# O (n * W)
def knapSack(weights, values, maxWeight):
    array = [[0 for x in range(maxWeight + 1)] for x in range(len(weights) + 1)]

    for index in range(n + 1):
        for weight in range(maxWeight + 1):

            if index == 0 or weight == 0:
                array[index][weight] = 0

            elif weights[index - 1] <= weight:
                array[index][weight] = max(values[index - 1] + array[index - 1][weight - weights[index - 1]], array[index - 1][weight])

            else:
                array[index][weight] = array[index - 1][weight]

    # for row in array:
    #     print(row)

    return array[len(weights)][maxWeight]

# Driver program to test above function
val = [6, 10, 12]
wt = [1, 2, 3]
W = 5
n = len(val)
print(knapSack(wt,val, W))
# Question: Given an array, write a function to find any subarray that sums to zero, if one
#  exists.

# Clarifications: Any array? Does it matter which one? what to return if not? Must be continous?

# Solution: Compute cumulative sum in separate array. Once you hit same number again, take all values from
#  old occurence + 1 to current location

# Complexity: O(n) time, O(n) space

def zero_sum_subarray(array) -> list[int]:

    if 0 in array:
        return [0]

    sums = [0 for x in range(len(array))]

    for x in range(len(array)):
        if x == 0:
            sums[x] = array[x]
        else:
            curr_sum = sums[x - 1] + array[x]
            if curr_sum in sums:
                first = sums.index(curr_sum)
                return array[first + 1:x + 1]
            else:
                sums[x] = curr_sum

    return []

array = [1, -3, -5, 1, 2, -3]
print(zero_sum_subarray(array))
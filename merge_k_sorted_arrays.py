# Question: Given k sorted arrays, merge them into a single sorted array.

# Clarifying Questions:

# Solution:
# 1: Merge all arrays and then sort
# 2: Next elements array, pointers array, and result. Iterate through, taking minimum, incrementing pointer,
#  and when reach end of an array set next to infinity. While length of set != 1

# Complexity:
# n is number of arrays, k is number of values
# 1: O(kn * log(kn))  # small n's are better (good for fewer but large arrays)
# 2: O(kn * k)  large n's, small K are better (good for many small arrays)
import math

def merge_k_sorted_arrays(arrays) -> list[int]:

    if [] in arrays:
        arrays = arrays.remove([])

    if not arrays or len(arrays) == 0:
        return []

    next_elements = [x[0] for x in arrays]
    pointers = [0 for x in range(len(arrays))]
    result = []
    # [1, 2, 3]
    # [1, 0, 0]

    while len(set(next_elements)) != 1:
        curr_min = min(next_elements)
        result.append(curr_min)
        index = next_elements.index(curr_min)
        pointers[index] += 1

        # If last element of array was just used
        if len(arrays[index]) == pointers[index]:
            next_elements[index] = math.inf
        else:
            next_elements[index] = arrays[index][pointers[index]]

    return result

print(merge_k_sorted_arrays([[1, 4, 7],[2, 5, 8],[3, 6, 9]])) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(merge_k_sorted_arrays([])) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(merge_k_sorted_arrays([[],[],[]])) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
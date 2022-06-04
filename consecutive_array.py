# Question: Given an unsorted array, find the length of the longest sequence of
# consecutive numbers in the array.

# Clarify: Clarify consecutive, do same numbers count

# Solution 1: Sort and then iterate through

# Time Complexity 1: O (nlogn) time, O(1) space

def consecutive_array(array) -> list[int]:
    curr_len = 1
    max_len = 1

    array.sort()

    for x in range(len(array)):
        if x != 0:
            if array[x] == array[x - 1] + 1:
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
            else:
                curr_len = 1

    return max_len



print(consecutive_array([4,2,1,6,5]))
print(consecutive_array([5,5,3,1]))
print(consecutive_array([2,6,3,1,5,7,4,3]))

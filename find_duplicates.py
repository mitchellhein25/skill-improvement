# Question: Given an array of integers where each value 1 <= x <= len(array), write a
# function that finds all the duplicates in the array.

# Due to the 1 <= x <= len(array), we can just iterate through and multiply the index of a value by -1 if we have
# seen it already. That would be O(n) time and O(1) space

# Solution: Sort the array, iterate through and if the current number equal the previous, append to results.

# Time Complexity: sort: O(nlogn) and O(n) to get duplicates

def find_duplicates(array) -> list[int]:
    result = []

    array.sort()

    is_dup = False
    for x in range(len(array)):

        curr = array[x]
        if x != 0:
            is_dup = curr == array[x - 1]

        if is_dup:
            if curr not in result:
                result.append(curr)

    return result

print(find_duplicates([1,2,3]))
print(find_duplicates([1,2,2]))
print(find_duplicates([3,3,3]))
print(find_duplicates([2,1,2,1,3,2,3,4,5,3,2,2,2,5]))
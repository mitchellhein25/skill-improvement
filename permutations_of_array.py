# Question: Write a function that returns all permutations of a given list.

# Clarifications:

# Solution: Backtracking approach. Pass results, visited, subset, and nums. Iterate through the len of nums, if i has
#  not been visited, add it to visited, call the recursive, then remove from visited

# Complexity: O(n!) time, O(3n) space

def permutations_of_array(nums) -> list[list[int]]:
    return backtracking([], [], [], nums)

def backtracking(res, visited, subset, nums):

    if len(subset) == len(nums):
        if subset not in res:
            res.append(subset)

    for i in range(len(nums)):
        if i not in visited:
            visited.append(i)
            backtracking(res, visited, subset + [nums[i]], nums)
            visited.remove(i)

    return res

array = [1,2,3]
print(permutations_of_array(array))
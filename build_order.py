# Question: Given a list of packages that need to be built and the dependencies for each
#  package, determine a valid order in which to build the packages.

# Clarifications: Any valid order? Optimal order? Will the dependencies always be valid?
#  what if there is a cycle, or if a dependency does not exist

# Solution:
#  Brute: Iterate through each value in the array and each time add the ones that aren't in result if dependencies
#  have been reached
#  Optimal: Topological sort: Temporary markers and permanent markers. If not in permanent, pass to recursive visit
#  function. If key is in temp, throw exception. If not in perm, add to temp, call recursive for each dependency,
#  then add to permanent and remove from temp

# Complexity:
#  Brute: O(n^2) time, O(n) space
#  Optimal: O(n) time, O(2n) space

temp_marks = []
perm_marks = []

def build_order(packages) -> list[int]:

    for key, value in packages.items():
        if key not in perm_marks:
            visit(key, packages)
    return perm_marks

def visit(key, packages) -> None:
    if key in temp_marks:
        raise Exception(f"Packages contains a cycle at package {key}")

    if key not in perm_marks:
        temp_marks.append(key)

        for pack in packages[key]:
            visit(pack, packages)

        perm_marks.append(key)
        temp_marks.remove(key)


# BRUTE FORCE SOLUTION
# def build_order(packages) -> list[int]:
#     if not packages:
#         return []
#
#     result = []
#     x = 0
#     while len(result) != len(packages):
#
#         for key, value in packages.items():
#             if value == []:
#                 if key not in result:
#                     result.append(key)
#
#             elif key not in result:
#                 ready = True
#                 for pack in value:
#                     if pack not in result:
#                         ready = False
#                 if ready:
#                     result.append(key)
#         x += 1
#     print(x)
#     return result

packages = {
    0: [],
    1: [0],
    2: [0],
    3: [1,2],
    4: [3]
}
# packages = {
#     0: [],
#     1: [2],
#     2: [0],
#     3: [4,2],
#     4: [1]
# }
print(build_order(packages))

# 0, 2, 1, 4, 3
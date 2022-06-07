# Question: Given a stack, reverse the items without creating any additional data
# structures.

# Clarifications: How is the stack implemented? We will assume an array.

# Solution: Call recursive until all values popped, then call helper to insert at bottom. In the insert at bottom,
#  append the original called value if empty, otherwise pop and call recursive again. Then append the currents again.

# Complexity: O(n^2) time, O(2n) space

def reverse_stack(stack: list[int]) -> list[int]:
    if not stack:
        return []

    curr = stack.pop()
    reverse_stack(stack)
    stack = insert_at_bottom(stack, curr)
    return stack


def insert_at_bottom(stack: list[int], val: int) -> list[int]:

    if not stack:
        stack.append(val)
        return stack

    curr = stack.pop()
    insert_at_bottom(stack, val)
    stack.append(curr)
    return stack


stack = [1,2,3] # [4,3,2,1]



print(reverse_stack(stack))
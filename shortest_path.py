# Question: Given a directed graph, find the shortest path between two nodes if one exists.

# Clarifications: Return the path? Not weighted, just looking for least edges?

# Solution: Breadth First Search, add to dictionary, read backwards for result

# Complexity: O(V + E) time, O(V) space

from collections import deque

def shortest_path(graph, start, end):
    parent = {start: None}

    queue = deque()
    queue.append(start)

    while queue:
        curr = queue.popleft()
        for val in graph[curr]:
            if val not in parent:
                parent[val] = curr
                queue.append(val)
    print(parent)
    result = []
    curr = end
    while curr:
        result.append(curr)
        curr = parent[curr]

    result.reverse()
    return result


graph = {1: [2, 1],
         2: [5],
         3: [],
         4: [1, 3],
         5: [4]}

print(shortest_path(graph, 1, 3))
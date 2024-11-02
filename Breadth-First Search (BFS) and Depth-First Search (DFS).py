from collections import deque, defaultdict

# Graph represented as an adjacency list
graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [0, 3, 4]
graph[2] = [0, 5]
graph[3] = [1]
graph[4] = [1, 5]
graph[5] = [2, 4]

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Depth-First Search (DFS)
def dfs(graph, start, visited=set()):
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Testing BFS and DFS
print("BFS traversal:")
bfs(graph, 0)  # Output: 0 1 2 3 4 5

print("\nDFS traversal:")
dfs(graph, 0)  # Output: 0 1 3 4 5 2

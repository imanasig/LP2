# Implement depth first search algorithm and Breadth First Search algorithm.
# Use an undirected graph and develop a recursive algorithm
# for searching all the vertices of a graph or tree data structure.

from collections import deque

# Function to add edge in undirected graph
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

    # Sort for consistent traversal
    graph[u].sort()
    graph[v].sort()

# DFS Traversal (Recursive)
def dfs_recursive(graph, current, visited, traversal):
    visited.add(current)
    traversal.append(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal)

# DFS Search with Recursive Path Tracking
def dfs_search(graph, current, target, visited, path):
    visited.add(current)
    path.append(current)
    # Target found
    if current == target:
        return True

    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs_search(graph, neighbor, target, visited, path):
                return True
    # Backtracking
    path.pop()

    return False

# BFS Traversal (Recursive)
def bfs_recursive(graph, queue, visited, traversal):
    if not queue:
        return
    # Remove first node
    node = queue.popleft()
    traversal.append(node)

    # Visit neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    bfs_recursive(graph, queue, visited, traversal)

# BFS Search with Recursive Path Tracking
def bfs_search_recursive(graph, queue, visited, target):
    if not queue:
        return None

    # Remove node and path
    node, path = queue.popleft()

    # Target found
    if node == target:
        return path

    # Visit neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(
                (neighbor, path + [neighbor])
            )

    return bfs_search_recursive(graph, queue, visited, target)

# MAIN PROGRAM
n = int(input("Enter number of vertices: "))

graph = {i: [] for i in range(n)}

e = int(input("Enter number of edges: "))

print("Enter edges (u v):")

for _ in range(e):
    u, v = map(int, input().split())
    add_edge(graph, u, v)

start = int(input("Enter starting vertex: "))

# DFS Traversal
visited = set()
dfs_result = []

dfs_recursive(graph, start, visited, dfs_result)

print("\nDFS Traversal:",
      " -> ".join(map(str, dfs_result)))

# BFS Traversal (Recursive)
visited = set()
visited.add(start)

queue = deque([start])

bfs_result = []

bfs_recursive(graph, queue, visited, bfs_result)

print("BFS Traversal:",
      " -> ".join(map(str, bfs_result)))

# Search Node
target = int(input("\nEnter node to search: "))

# DFS Search Path
visited = set()
dfs_path = []

if dfs_search(graph, start, target, visited, dfs_path):
    print("DFS Path:",
          " -> ".join(map(str, dfs_path)))
else:
    print("Node not found using DFS")

# BFS Search Path (Recursive)
visited = set()
visited.add(start)

queue = deque([(start, [start])])

bfs_path = bfs_search_recursive(
    graph,
    queue,
    visited,
    target
)

if bfs_path is not None:
    print("BFS Path:",
          " -> ".join(map(str, bfs_path)))
else:
    print("Node not found using BFS")

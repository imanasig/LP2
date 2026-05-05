#Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure.
from collections import deque

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)
    
    graph[u].sort()
    graph[v].sort()

# DFS Traversal (Recursive)
def dfs_recursive(graph, current, visited, traversal):
    visited.add(current)
    traversal.append(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal)

# DFS Search with Path
def dfs_search(graph, current, target, visited, path):
    visited.add(current)
    path.append(current)

    if current == target:
        return True

    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs_search(graph, neighbor, target, visited, path):
                return True

    path.pop() 
    return False

# BFS Traversal
def bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []

    visited.add(start)

    while queue:
        node = queue.popleft()
        traversal.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal

# BFS Search with Path
def bfs_search(graph, start, target):
    visited = set()
    queue = deque([(start, [start])])

    visited.add(start)

    while queue:
        node, path = queue.popleft()

        if node == target:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

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
print("\nDFS Traversal:", " -> ".join(map(str, dfs_result)))

# BFS Traversal
bfs_result = bfs_traversal(graph, start)
print("BFS Traversal:", " -> ".join(map(str, bfs_result)))

# Search node
target = int(input("\nEnter node to search: "))

# DFS Path
visited = set()
dfs_path = []
if dfs_search(graph, start, target, visited, dfs_path):
    print("DFS Path:", " -> ".join(map(str, dfs_path)))
else:
    print("Node not found using DFS")

# BFS Path
bfs_path = bfs_search(graph, start, target)
if bfs_path is not None:
    print("BFS Path:", " -> ".join(map(str, bfs_path)))
else:
    print("Node not found using BFS")

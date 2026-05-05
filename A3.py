# I. Selection Sort (Greedy)
def selection_sort():
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print("Sorted Array:", arr)

# II. Minimum Spanning Tree (Simple Greedy Idea) (Using edge selection - demonstration)
def simple_mst():
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    edges = []
    print("Enter edges (u v w):")
    for _ in range(e):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort()

    selected = []
    visited = set()

    for w, u, v in edges:
        if u not in visited or v not in visited:
            selected.append((u, v, w))
            visited.add(u)
            visited.add(v)

    print("Selected edges (MST approx):", selected)

# III. Single Source Shortest Path (Greedy - Basic)
def single_source_shortest_path():
    n = int(input("Enter number of vertices: "))
    graph = [[] for _ in range(n)]

    e = int(input("Enter number of edges: "))
    print("Enter edges (u v w):")
    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    start = int(input("Enter source vertex: "))

    dist = [9999] * n
    visited = [False] * n

    dist[start] = 0

    for _ in range(n):
        u = -1
        min_dist = 9999

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        visited[u] = True

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    print("Shortest distances:", dist)

# IV. Job Scheduling (Greedy)
def job_scheduling():
    n = int(input("Enter number of jobs: "))

    jobs = []
    print("Enter jobs (id deadline profit):")
    for _ in range(n):
        job_id, deadline, profit = input().split()
        jobs.append((job_id, int(deadline), int(profit)))

    # Sort by profit descending
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * (max_deadline + 1)

    total_profit = 0

    for job in jobs:
        for j in range(job[1], 0, -1):
            if slots[j] is None:
                slots[j] = job[0]
                total_profit += job[2]
                break

    print("Scheduled Jobs:", [job for job in slots if job])
    print("Total Profit:", total_profit)

# V. Prim's Algorithm (MST)
def prims():
    n = int(input("Enter number of vertices: "))
    graph = [[0]*n for _ in range(n)]

    print("Enter adjacency matrix:")
    for i in range(n):
        graph[i] = list(map(int, input().split()))

    selected = [False] * n
    selected[0] = True

    print("Edges in MST:")

    for _ in range(n - 1):
        min_val = 9999
        x = y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j] < min_val:
                            min_val = graph[i][j]
                            x, y = i, j

        print(x, "-", y, ":", graph[x][y])
        selected[y] = True

# VI. Kruskal's Algorithm (MST)
def kruskal():

    def find(parent, i):
        while parent[i] != i:
            i = parent[i]
        return i

    def union(parent, x, y):
        parent[x] = y

    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    edges = []
    print("Enter edges (u v w):")
    for _ in range(e):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort()

    parent = [i for i in range(n)]
    mst = []

    for w, u, v in edges:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            mst.append((u, v, w))
            union(parent, x, y)

    print("Edges in MST:", mst)

# VII. Dijkstra's Algorithm
def dijkstra():
    n = int(input("Enter number of vertices: "))
    graph = [[0]*n for _ in range(n)]

    print("Enter adjacency matrix:")
    for i in range(n):
        graph[i] = list(map(int, input().split()))

    start = int(input("Enter source vertex: "))

    dist = [9999] * n
    visited = [False] * n

    dist[start] = 0

    for _ in range(n):
        min_val = 9999
        u = -1

        for i in range(n):
            if not visited[i] and dist[i] < min_val:
                min_val = dist[i]
                u = i

        visited[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    print("Shortest distances:", dist)

# Uncomment ONLY what you need in exam

# selection_sort()
# simple_mst()
# single_source_shortest_path()
# job_scheduling()
# prims()
# kruskal()
# dijkstra()
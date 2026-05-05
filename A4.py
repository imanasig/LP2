# I. N-Queens using Backtracking
def n_queens_backtracking():
    n = int(input("Enter value of N: "))
    board = [[0]*n for _ in range(n)]

    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check left diagonal
        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check right diagonal
        i, j = row-1, col+1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                if solve(row + 1):
                    return True
                board[row][col] = 0

        return False

    if solve(0):
        print("Solution:")
        for row in board:
            print(row)
    else:
        print("No solution exists")

# II. N-Queens using Branch and Bound
def n_queens_branch_bound():
    n = int(input("Enter value of N: "))
    board = [[0]*n for _ in range(n)]

    col = [False]*n
    diag1 = [False]*(2*n)
    diag2 = [False]*(2*n)

    def solve(row):
        if row == n:
            return True

        for c in range(n):
            if not col[c] and not diag1[row+c] and not diag2[row-c+n]:
                board[row][c] = 1
                col[c] = diag1[row+c] = diag2[row-c+n] = True

                if solve(row+1):
                    return True

                board[row][c] = 0
                col[c] = diag1[row+c] = diag2[row-c+n] = False

        return False

    if solve(0):
        print("Solution:")
        for row in board:
            print(row)
    else:
        print("No solution exists")

# III. Graph Coloring using Backtracking
def graph_coloring():
    n = int(input("Enter number of vertices: "))
    
    graph = []
    print("Enter adjacency matrix:")
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    m = int(input("Enter number of colors: "))
    color = [0]*n

    def is_safe(v, c):
        for i in range(n):
            if graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def solve(v):
        if v == n:
            return True

        for c in range(1, m+1):
            if is_safe(v, c):
                color[v] = c

                if solve(v+1):
                    return True

                color[v] = 0

        return False

    if solve(0):
        print("Color assignment:", color)
    else:
        print("No solution exists")


print("Choose an option:")
print("1. N-Queens (Backtracking)")
print("2. N-Queens (Branch and Bound)")
print("3. Graph Coloring")
choice = int(input("Enter your choice: "))
if choice == 1:
    n_queens_backtracking()
elif choice == 2:
    n_queens_branch_bound()
elif choice == 3:
    graph_coloring()
else:
    print("Invalid choice")
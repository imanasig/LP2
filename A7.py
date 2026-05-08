#Using C++/Java/Python, implement A* algorithm for n-queen problem.
def heuristic(state):

    h = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            # Same column
            if state[i] == state[j]:
                h += 1
            # Same diagonal
            elif abs(state[i] - state[j]) == abs(i - j):
                h += 1
    return h

# Generate Neighbor States
def generate_neighbors(state):
    neighbors = []
    n = len(state)

    for row in range(n):

        for col in range(n):

            # Skip same position
            if state[row] != col:

                new_state = state[:]
                new_state[row] = col

                neighbors.append(new_state)
    return neighbors

# Print Chess Board
def print_board(state):
    n = len(state)
    for i in range(n):
        for j in range(n):
            if state[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# A* Algorithm
def a_star_nqueen(n):
    # Initial state
    start_state = [0] * n
    open_list = []
    # state, g, h, f
    h = heuristic(start_state)
    open_list.append((start_state, 0, h, h))
    visited = []

    while len(open_list) > 0:
        # Select state with minimum f(n)
        current_index = 0

        for i in range(len(open_list)):
            if open_list[i][3] < open_list[current_index][3]:
                current_index = i

        current_state, g, h, f = open_list.pop(current_index)
        # Goal check
        if h == 0:
            return current_state
        visited.append(current_state)

        # Generate neighbors
        neighbors = generate_neighbors(current_state)
        for neighbor in neighbors:
            if neighbor not in visited:
                new_g = g + 1
                new_h = heuristic(neighbor)

                # f(n) = g(n) + h(n)
                new_f = new_g + new_h

                open_list.append(
                    (neighbor, new_g, new_h, new_f)
                )
    return None

# MAIN PROGRAM
n = int(input("Enter value of N: "))
solution = a_star_nqueen(n)
# Output
if solution:
    print("\nSolution Found:\n")
    print_board(solution)
else:
    print("No solution found")

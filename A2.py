#Implement A star Algorithm for any game search problem.
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Function to calculate Manhattan Distance (heuristic)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Function to find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Function to copy state
def copy_state(state):
    new_state = []
    for row in state:
        new_state.append(row[:])
    return new_state

# Generate neighbors
def generate_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy_state(state)
            # swap blank with neighbor
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

# Function to convert state to tuple (for visited check)
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

# A* Algorithm
def a_star(start):

    open_list = []   # list of nodes: (state, g, h, f, path)
    closed_set = set()

    h = heuristic(start)
    open_list.append((start, 0, h, h, [start]))

    while len(open_list) > 0:

        current_index = 0
        for i in range(len(open_list)):
            if open_list[i][3] < open_list[current_index][3]:
                current_index = i

        current, g, h, f, path = open_list.pop(current_index)

        if current == goal_state:
            return path

        closed_set.add(state_to_tuple(current))

        for neighbor in generate_neighbors(current):
            if state_to_tuple(neighbor) in closed_set:
                continue

            new_g = g + 1
            new_h = heuristic(neighbor)
            new_f = new_g + new_h

            open_list.append((neighbor, new_g, new_h, new_f, path + [neighbor]))

    return None

print("Enter initial state (3x3 matrix, use 0 for blank):")

start_state = []
for i in range(3):
    row = list(map(int, input().split()))
    start_state.append(row)

solution = a_star(start_state)

if solution is None:
    print("No solution found")
else:
    print("\nSolution found in", len(solution) - 1, "moves:\n")

    for step in solution:
        for row in step:
            print(row)
        print()

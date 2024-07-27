import pulp
import math

# City coordinates
coordinates = [
    (8, 11),   # depot
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

n = len(coordinates)

# Calculate the Euclidean distance between each pair of nodes
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem variable to contain the problem data
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints ensuring each city is left and entered exactly once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_city_{i}"
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_city_{i}"

# Subtour elimination - method: adding constraint for every subset not functionally feasible, so use a lazy constraints approach

# Solving the problem
model.solve()

# Gather results if an optimal solution was found
if pulp.LpStatus[model.status] == 'Optimal':
    # Find tour path
    path = []
    start = 0
    current = start
    while True:
        path.append(current)
        next_moves = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
        if not next_moves:
            break
        current = next_moves[0]
    path.append(start)  # Complete the cycle

    # Calculate total travel cost
    total_cost = sum(cost[path[i]][path[i+1]] for i in range(len(path)-1))

    print(f"Tour: {path}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")
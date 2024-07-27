import math
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpStatus, PULP_CBC_CMD

# Define the coordinates including the depot
coordinates = [
    (30, 56),
    (53, 42),
    (1, 95),
    (25, 61),
    (69, 57),
    (6, 58),
    (12, 84),
    (72, 77),
    (98, 95),
    (11, 0),
    (61, 25),
    (52, 0),
    (60, 95),
    (10, 94),
    (96, 73),
    (14, 47),
    (18, 16),
    (4, 43),
    (53, 76),
    (19, 72)
]

# Number of cities
n = len(coordinates)

# Function to calculate Euclidean distance
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Define the problem
model = LpProblem("TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = Lp.SupplyVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective
model += lpSum(x[i, j] * distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1) * x[i, j] <= n - 2

# Solve the model
model.solve(PULP_CBC_CMD(msg=0))

# Check if a solution exists
if LpStatus[model.status] == 'Optimal':
    active_edges = [(i, j) for i in range(n) for j in range(n) if i != j and x[i, j].varValue == 1]
    tour = []
    current = 0
    tour.append(current)
    while len(active_edges) > 0:
        for i, j in active_edges:
            if i == current:
                tour.append(j)
                active_edges.remove((i, j))
                current = j
                break

    # Return to start
    tour.append(tour[0])
    
    # Calculate travel cost and maximum distance
    total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    max_cost = max(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_cost)
else:
    print("No feasible solution was found.")
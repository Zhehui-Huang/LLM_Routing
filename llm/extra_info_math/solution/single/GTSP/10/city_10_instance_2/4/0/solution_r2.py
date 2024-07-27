from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD
from math import sqrt

coordinates = [
    (90, 3),   # Depot 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

city_groups = [
    [3, 6],    # Group 0
    [5, 8],    # Group 1
    [4, 9],    # Group 2
    [1, 7],    # Group 3
    [2]        # Group 4
]

# Calculate distance
def euclidean_distance(a, b):
    return sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Initialize the optimization problem
model = LpProblem("TSP", LpMinimize)

# Variables: x_ij where i, j are cities
x = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            x[(i, j)] = LpVariable(f"x_{i}_{j}", 0, 1, cat='Binary')

# Objective
model += lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraint: Each group should have exactly 1 connection with the depot or another group
for group in city_groups:
    model += lpSum(x[(i, j)] for i in range(10) for j in group if i != j) == 1
    model += lpSum(x[(j, i)] for i in range(10) for j in group if i != j) == 1

# Constraints: Every city is entered and exited only once
for k in range(10):
    model += lpSum(x[(i, k)] for i in range(10) if i != k) == lpSum(x[(k, j)] for j in range(10) if j != k)

# Solve the model
model.solve(PULP_CBC_CMD(msg=0))

# Extract the solution
tour = [0]
current = 0
for _ in range(len(coordinates)):
    for j in range(len(coordinates)):
        if j != current and x[(current, j)].varValue == 1:
            tour.append(j)
            current = j
            break
    if current == 0:
        break

# Calculate total travel cost
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
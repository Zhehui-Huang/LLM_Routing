import pulp
import math
from itertools import product

# Define cities and their coordinates
coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Number of robots (salesmen)
num_robots = 2
depots = [0, 1]

# Calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Generate cost matrix
cost_matrix = {}
for i, j in product(coordinates, repeat=2):
    cost_matrix[(i, j)] = euclidean_array[i,:,j] = euclidean_distance(coordinates[i], coordinates[j])

# Model initialization
model = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Variables x_{ijk} where i != j and k is a depot
x_vars = {}
for k in depots:
    for i in coordinates:
        for j in coordinates:
            if i != j:
                x_vars[(i, j, k)] = pulp.LpVariable(f"x_{i}_{j}_{k}", cat="Binary")

# Objective function
model += pulp.lpSum(cost_matrix[i, j] * x_vars[i, j, k] for k in depots for i in coordinates for j in coordinates if i != j)

# Constraints
# Each node must be arrived at exactly once
for j in coordinates:
    if j not in depots:
        model += pulp.lpSum(x_vars[i, j, k] for k in depots for i in coordinates if i != j) == 1

# Departing from depot constraints
for k in depots:
    model += pulp.lpSum(x_vars[k, j, k] for j in coordinates if k != j) == 1
    model += pulp.lpSum(x_vars[j, k, k] for j in coordinates if k != j) == 1

# Route continuity constraints
for k in depots:
    for i in coordinates:
        if i not in depots:
            model += pulp.lpSum(x_vars[h, i, k] for h in coordinates if h != i) == pulp.lpSum(x_vars[i, j, k] for j in coordinates if i != j)

# Solve model
model.solve()

# Extracting the results
routes = {k: [] for k in depots}
for k in depots:
    start = k
    while True:
        for j in coordinates:
            if j != start and pulp.value(x_vars[start, j, k]) == 1:
                routes[k].append(start)
                start = j
                break
        if start == k:
            routes[k].append(start)
            break

# Calculating costs
costs = {}
for k in depots:
    route_cost = sum(cost_matrix[routes[k][i], routes[k][i+1]] for i in range(len(routes[k])-1))
    costs[k] = route_cost

# Output results
total_cost = sum(costs.values())
for k in depots:
    print(f"Robot {k} Tour: {routes[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Overall Total Travel Cost: {total_cost}")
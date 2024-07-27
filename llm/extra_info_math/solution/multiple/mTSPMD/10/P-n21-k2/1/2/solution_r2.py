import pulp
import math
from itertools import product

# Cities and their coordinates
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

# Function to compute Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost matrix between every pair of nodes
cost_matrix = {(i, j): euclidean_distance(coordinates[i], coordinates[j])
               for i in coordinates for j in coordinates if i != j}

# Initialize the problem
model = pulp.LpProblem("MDVRP", pulp.LpMinimize)

# Define variables: x_{ij}^{k} = 1 if route goes from i to j on vehicle k
x_vars = pulp.LpVariable.dicts("x",
                               ((i, j, k) for k in [0, 1]
                                for i in coordinates for j in coordinates if i != j),
                               lowBound=0, upBound=1, cat='Binary')

# Objective: Minimize total distance
model += pulp.lpSum(cost_matrix[i, j] * x_vars[(i, j, k)]
                    for k in [0, 1] for i in coordinates for j in coordinates if i != j), "Total_Cost"

# Constraint: Enter and leave each non-depot city exactly once
for k in [0, 1]:
    for j in coordinates:
        if j != k:
            model += pulp.lpSum(x_vars[(i, j, k)] for i in coordinates if i != j) == 1, f"Enter_{j}_on_{k}"
            model += pulp.lpSum(x_vars[(j, i, k)] for i in coordinates if i != j) == 1, f"Leave_{j}_on_{k}"

# Constraint: Leave each depot exactly once and come back
for k in [0, 1]:
    model += pulp.lpSum(x_vars[(k, j, k)] for j in coordinates if j != k) == 1, f"Leave_Depot_{k}"
    model += pulp.lpSum(x_vars[(j, k, k)] for j in coordinates if j != k) == 1, f"Return_to_Depot_{k}"

# Solve the problem
model.solve()

# Check status and show the total distance if solved
solution_status = pulp.LpStatus[model.status]
if solution_status == 'Optimal':
    # Retrieve the paths and calculate their costs
    paths = {k: [] for k in [0, 1]}
    path_costs = {k: 0 for k in [0, 1]}
    for k in [0, 1]:
        current_location = k
        paths[k].append(current_location)
        tour_cost = 0
        while True:
            # In a real-world scenario you might need other stopping criteria
            next_locations = [(j, cost_matrix[current_location, j]) for j in coordinates
                              if j != current_location and pulp.value(x_vars[current_location, j, k]) == 1]
            if not next_locations:
                break
            next_location, cost = min(next_locations, key=lambda x: x[1])
            paths[k].append(next_location)
            tour_cost += cost
            current_location = next_location
            if current_location == k:
                break
        paths[k].append(k)  # return to depot
        path_costs[k] = tour_value

    for k in paths:
        print(f"Robot {k} Tour: {paths[k]}")
        print(f"Robot {k} Total Travel Cost: {path_costs[k]}")

    overall_cost = sum(path_costs.values())
    print(f"Overall Total Travel Cost: {overall_cost}")
else:
    print(f"No optimal solution available: {solution_status}")
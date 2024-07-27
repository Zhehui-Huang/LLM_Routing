import pulp
import math
from itertools import product

# City coordinates
coordinates = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Group information: each group must have one city visited
groups = {
    0: [1, 4],
    1: [2, 6],
    2: [7],
    3: [5],
    4: [9],
    5: [8],
    6: [3]
}

# Calculate Euclidean distances
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Cost matrix
num_cities = len(coordinates)
costs = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Integer programming
problem = pulp.LpProblem("TSP_Group_Variant", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(num_cities) for j in range(num_cities)], cat=pulp.LpBinary)

# Objective
problem += pulp.lpSum(costs[i][j] * x[i, j] for i in range(num_cities) for j in range(num_cities)), "Minimize_Total_Cost"

# Constraints
for group_indices in groups.values():
    # Outgoing
    problem += pulp.lpSum(x[i, j] for i in group_indices for j in range(num_cities) if j not in group_indices) == 1
    # Incoming
    problem += pulp.lpSum(x[j, i] for i in group_indices for j in range(num_cities) if j not in group_indices) == 1

# Flow conservation
for k in range(num_cities):
    problem += pulp.lpSum(x[i, k] for i in range(num_cities) if i != k) == pulp.lpSum(x[k, j] for j in range(num_cities) if j != k), f"Flow_Conservation_{k}"

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Fetch solution
if status == pulp.LpStatusOptimal:
    tour = []
    visited = set()
    current = 0
    while True:
        visited.add(current)
        tour.append(current)
        next_city = next(j for j in range(num_cities) if pulp.value(x[current, j]) == 1)
        if next_city == 0:
            tour.append(0)
            break
        current = next_city

    total_cost = pulp.value(problem.objective)

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("Failed to find an optimal solution.")
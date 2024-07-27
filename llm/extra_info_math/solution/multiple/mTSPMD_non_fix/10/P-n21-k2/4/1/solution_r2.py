from pulp import *
import itertools
from math import sqrt

# Defining problem data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
depots = [0, 1]
n_robots = 2  # 2 Robots, one in each depot theoretically, although initial definition is confusing

def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Model setup
model = LpProblem("Vehicle_Routing_Problem", LpMinimize)

x = LpVariable.dicts("x", [(i, j) for i in range(21) for j in range(21) if i != j], cat='Binary')
u = LpVariable.dicts("u", range(21), lowBound=0, cat='Continuous')

# Objective
model += lpSum([euclidean_distance(coordinates[i], coordinates[j]) * x[(i, j)] for i, j in x]), "Total Travel"

# Constraints
for j in range(21):
    model += lpSum([x[(i, j)] for i in range(21) if i != j]) == 1, f"Arrival_{j}"
    model += lpSum([x[(j, k)] for k in range(21) if j != k]) == 1, f"Departure_{j}"

# Subtour elimination
for i in range(1, 21):
    for j in range(1, 21):
        if i != j:
            model += u[i] - u[j] + 21 * x[(i, j)] <= 20, f"Eliminate_Subtour_{i}_{j}"

# Solve the problem
model.solve()

# Print results
tour_paths = {}
for k in depots:
    tour_paths[k] = []
    next_city = k
    while True:
        next_city = next((j for i, j in x if i == next_city and value(x[(i, j)]) == 1), None)
        if next_city is None or next_city in depots:
            break
        tour_paths[k].append(next_city)

total_cost = 0
for k in tour_paths:
    print(f"Robot {k} starting at {k} Tour: [{k}] + {tour_paths[k]}")
    tour_cost = sum(euclidean_distance(coordinates[i], coordinates[tour_paths[k][idx + 1 if idx + 1 < len(tour_paths[k]) else 0]]) for idx, i in enumerate(tour_paths[k][:-1]))
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")
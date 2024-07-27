import pulp
import math
from itertools import product
import numpy as np

# Cities and their coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
                (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
                (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Depots corresponding to indices
depots = [0, 1]

# Calculate Euclidean Distance
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Define distances between cities
distances = {(i, j): euclidean distance(coordinates[i], coordinates[j]) for i, j in product(range(21), repeat=2)}

# Create the problem
problem = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Decision variables: x[i, j] is 1 if travel from i to j occurs
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(21) for j in range(21)], cat='Binary')

# Objective: Minimize the total distance
problem += pulp.lpSum(distances[i, j] * x[i, j] for i in range(21) for j in range(21))

# Constraints
# Each city must be left exactly once
for j in range(21):
    problem += pulp.lpSum(x[i, j] for i in range(21)) == 1

# Each city must be entered exactly once
for i in range(21):
    problem += pulp.lpSum(x[i, j] for j in range(21)) == 1

# Multiple robots - partitioning the tours from starting depots (handling subtours)
u = pulp.LpVariable.dicts("u", range(21), lowBound=0, upBound=20, cat='Continuous') # position variables to eliminate subtours

for i in range(1, 21):
    for j in range(1, 21):
        if i != j:
            problem += u[i] - u[j] + 21 * x[i, j] <= 20

# Solve the problem
problem.solve()

# Parse the solution
routes = {i: [] for i in depots}
for i in range(21):
    for j in range(21):
        if x[i, j].varValue == 1:
            if i in depots:
                routes[i].append(j)

# Following the path to generate full routes for each depot
for depot in routes.keys():
    next_node = routes[depot][-1]
    while next_node not in depots:
        for k in range(21):
            if x[next_node, k].varValue == 1:
                routes[depot].append(k)
                next_node = k
                break

# Compute cost of each route
costs = {}
for depot, route in routes.items():
    cost = sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1))
    costs[depot] = cost
    print(f"Robot {depot} Tour: [{', '.join(map(str, route))}]")
    print(f"Robot {depot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {sum(costs.values())}")
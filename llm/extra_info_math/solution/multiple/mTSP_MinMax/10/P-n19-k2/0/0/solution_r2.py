from pulp import *
import math

# Define the city coordinates including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Total number of nodes (cities including depot)
n = len(coordinates)

# Number of robots (salesmen)
m = 2

# Problem
prob = LpProblem("TSP", LpMinimize)

# Creating a distance matrix for all city pairs
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i, j] = distance(coordinates[i], coordinates[j])

# Variables
x = LpVariable.dicts("x", [(i, j, k) for k in range(m) for i in range(n) for j in range(n) if i != j], cat='Binary')

# Objective function
prob += lpSum(x[i, j, k]*distances[i, j] for k in range(m) for i in range(n) for j in range(n) if i != j)

# Constraints

# Each city must be visited exactly once by exactly one robot
for j in range(1, n):
    prob += lpSum(x[i, j, k] for k in range(m) for i in range(n) if i != j) == 1

# Each robot must start and end at the depot
for k in range(m):
    prob += lpSum(x[0, j, k] for j in range(1, n)) == 1  # leave depot
    prob += lpSum(x[i, 0, k] for i in range(1, n)) == 1  # enter depot

# Continuity within each robot's tour, prevents subtours
for k in range(m):
    for j in range(1, n):
        prob += lpSum(x[i, j, k] for i in range(n) if i != j) == lpSum(x[j, i, k] for i in range(n) if i != j)

# Solve the LP
prob.solve()

# Extract solution
for k in range(m):
    tour = []
    for i in range(n):
        for j in range(n):
            if i != j and x[i, j, k].varValue == 1:
                tour.append((i, j))
    # Printing tour route for each robot
    print(f"Robot {k+1} tour:")
    start = 0  # starting at depot
    route = [start]
    while len(tour) > 0:
        for i, path in enumerate(tour):
            if path[0] == start:
                route.append(path[1])
                start = path[1]
                tour.pop(i)
                break
    print(route)
import math
from pulp import *

# Definition of cities (index, x-coordinate, y-coordinate)
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Number of cities
n = len(cities)

# Distance matrix
dist = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the model
model = LpProblem("TSP", LpMinimize)

# Decision variable x_ij, where x_ij = 1 if we travel from i to j, else 0
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')

# Auxiliary variable to minimize the maximum distance
d_max = LpVariable("d_max", lowBound=0)

# Objective: minimize the maximum distance between consecutive cities
model += d_max

# Constraints
for i in range(n):
    model += lpSum(x[i, j] for j in range(n) if i != j) == 1    # leave city i
    model += lpSum(x[j, i] for j in range(n) if i != j) == 1    # enter city i

# Maximum distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * dist[i][j] <= d_max

# Solve the problem
status = model.solve(PULP_CBC_CMD(msg=False))

# Check if a valid solution has been found
if LpStatus[model.status] == 'Optimal':
    # Extract tour
    tour = []
    cur_city = 0
    steps = 0
    while cur_city not in tour or steps == 0:
        next_moves = [(j) for j in range(n) if value(x[cur_city, j]) == 1]
        next_city = next_moves[0]
        tour.append(cur_city)
        cur_city = next_city
        steps += 1
    tour.append(0)  # to complete the tour by returning to origin

    # Calculate tour total travel cost
    total_cost = sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    # Calculate the maximum distance between consecutive cities in the tour
    max_distance = max(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("Failed to find optimal solution")
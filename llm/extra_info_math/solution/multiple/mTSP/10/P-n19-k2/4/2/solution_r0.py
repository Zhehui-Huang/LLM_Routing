import math
from pulp import *

# City coordinates, excluding the depot which is assumed to be city 0
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
               (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
               (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Number of robots and total number of cities (including depot)
m = 2
n = len(coordinates)

# Calculate Euclidean distances between all pairs of cities
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
cost_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# MTSP model
model = LpProblem("Multiple_TSP_Problem", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], 0, 1, LpBinary)
u = LpVariable.dicts("u", list(range(1, n)), lowBound=0, cat=LpContinuous)

# Objective function
model += lpSum(cost_matrix[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
for k in range(m):
    model += lpSum(x[0, j, k] for j in range(1, n)) == 1  # Each robot leaves the depot
    model += lpSum(x[i, 0, k] for i in range(1, n)) == 1  # Each robot returns to the depot

for j in range(1, n):
    model += lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1  # Each city is visited exactly once

for k in range(m):
    for i in range(1, n):
        model += lpSum(x[i, j, k] for j in range(n) if i != j) - lpSum(x[j, i, k] for j in range(n) if i != j) == 0  # Flow conservation
        
# Subtour Elimination Constraints
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
model.solve()

# Extract the solution
routes = {k: [] for k in range(m)}
for k in range(m):
    tour = []
    for i in range(n):
        for j in range(n):
            if x[i, j, k].varValue == 1:
                tour.append((i, j))
    # Sort to make the tour start from depot
    current_location = 0
    next_location = None
    while len(tour) > 0:
        for i, t in enumerate(tour):
            if t[0] == current_location:
                next_location = t[1]
                routes[k].append(t[0])
                current_location = next_location
                del tour[i]
                break
    routes[k].append(0)  # add depot back as the end

# Calculate travel costs
total_cost = 0
for k in range(m):
    cost = sum(cost_matrix[routes[k][i]][routes[k][i + 1]] for i in range(len(routes[k]) - 1))
    print(f"Robot {k} Tour: {routes[k]}")
    print(f"Robot {k} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")
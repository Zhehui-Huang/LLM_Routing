import pulp
import math
from itertools import product

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Number of robots and depots
num_robots = 8
depots = list(range(num_robots))  # Depots are at the first 8 cities

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost (distance) matrix
n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the optimization model
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in depads], cat=pulp.LpBinary)

# Objective function
model += pulp.lpSum(distances[i][j] * x[i, j, k] for i, j, k in x if i != j)

# Constraints

# Each city is visited exactly once by exactly one robot
for j in range(n):
    if j not in depots:
        model += pulp.lpSum(x[i, j, k] for i in range(n) for k in depots if i != j) == 1
        model += pulp.lpSum(x[j, i, k] for i in range(n) for k in depots if i != j) == 1

# Each robot leaves and enters its starting depot
for k in depots:
    model += pulp.lpSum(x[k, j, k] for j in range(n) if j != k) == 1  # leave once
    model += pulp.lpSum(x[j, k, k] for j in range(n) if j != k) == 1  # enter once

# Sub-tour elimination (MTZ constraints)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, cat=pulp.LpInteger)
for i, j, k in x:
    if i != j and i != k and j != k:
        model += u[i] - u[j] + (n - 1) * x[i, j, k] <= (n - 2)

# Solve the model
model.solve()

# Process results
tours = {k: [] for k in depots}
for k in depots:
    start = k
    next_city = start
    while True:
        next_moves = [j for j in range(n) if pulp.value(x[next_city, j, k]) == 1]
        if not next_moves:
            break
        next_city = next_moves[0]
        if next_city == start:
            break
        tours[k].append(next_city)

for k in tours:
    print(f"Robot {k} Tour: {tours[k]}")
    cost = sum(distances[tours[k][i]][tours[k][i + 1]] for i in range(len(tours[k]) - 1))
    print(f"Robot {k} Total Travel Cost: {cost}")

overall_cost = sum(distances[tours[k][i]][tours[k][i + 1]] for k in tours for i in range(len(tours[k]) - 1))
print(f"Overall Total Travel Cost: {overall_cost}")
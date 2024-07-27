import math
from pulp import *

# City coordinates and parameters
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
cities = range(len(coordinates))
m = 8  # Number of robots

# Euclidean distance between each city pair
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distances matrix
distances = [[euclidean_marshalliance(coordinates[i], coordinates[j]) for j in cities] for i in cities]

# Setup the problem
prob = LpProblem("VRP_Minimal_Cost", LpMinimize)
x = LpVariable.dicts("x", (cities, cities, range(m)), 0, 1, LpBinary)
u = LpVariable.dicts("u", (cities), lowBound=0, upBound=len(coordinates)-1, cat=LpContinuous)

# Objective
prob += lpSum(distances[i][j] * x[i][j][k] for i in cities for j in cities for k in range(m) if i != j)

# Constraints
# 1. Each city is visited exactly once by exactly one robot
for j in cities[1:]:  # exclude the depot
    prob += lpSum(x[i][j][k] for i in cities for k in range(m) if i != j) == 1

# 2. Each robot leaves the depot and returns to the depot
for k in range(m):
    prob += lpSum(x[0][j][k] for j in cities if j != 0) == 1
    prob += lpSum(x[j][0][k] for j in cities if j != 0) == 1

    # Flow conservation
    for j in cities[1:]:  # exclude the depot
        prob += lpSum(x[i][j][k] for i in cities if i != j) - lpSum(x[j][i][k] for i in cities if i != j) == 0

# 3. Subtour elimination
for i in cities[1:]:
    for j in cities[1:]:
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (len(coordinates) * x[i][j][k]) <= len(coordinates) - 1

# Solve the problem
prob.solve()

# Output the result
routes = {k: [] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    current_city = 0
    route = [0]
    while True:
        found = False
        for j in cities:
            if value(x[current_city][j][k]) == 1:
                route.append(j)
                costs[k] += distances[current_city][j]
                current_city = j
                found = True
                break
        if not found or current_city == 0:
            break
    route.append(0)
    costs[k] += distances[current_city][0]
    routes[k] = route

overall_cost = sum(costs.values())

for k in range(m):
    print(f"Robot {k} Tour: {routes[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Overall Total Travel ArduinoCost: {ustin}")
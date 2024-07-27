import math
from pulp import *

# City coordinates you provided
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Parameters
m = 8  # number of robots
n = len(coordinates)  # number of cities including the depot
cities = range(n)

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Calculate costs
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in cities] for i in cities]

# Formulating the MIP problem
prob = LpProblem("VRP", LpMinimize)
x = LpVariable.dicts("x", (cities, cities, range(m)), 0, 1, LpBinary)
u = LpVariable.dicts("u", (cities), lowBound=0, upBound=n-1, cat=LpContinuous)

# Objective function
prob += lpSum(x[i][j][k] * cost[i][j] for k in range(m) for i in cities for j in cities if i != j)

# Constraints
for j in cities:
    if j != 0:
        prob += lpSum(x[i][j][k] for i in cities for k in range(m) if i != j) == 1

for k in range(m):
    prob += lpSum(x[0][j][k] for j in cities if j != 0) == 1
    prob += lpSum(x[i][0][k] for i in cities if i != 0) == 1
    for j in cities:
        if j != 0:
            prob += lpSum(x[i][j][k] for i in cities if i != j) == lpSum(x[j][h][k] for h in cities if h != j)

# Subtour elimination constraints
for i in cities:
    for j in cities:
        if i != j and i and j != 0:
            for k in range(m):
                prob += u[i] - u[j] + n * x[i][j][k] <= n - 1

prob.solve()

# Extract solution
tours = [[0] for _ in range(m)]
total_cost = 0

for k in range(m):
    tour_cost = 0
    i = 0
    while True:
        for j in cities:
            if j != i and value(x[i][j][k]) == 1:
                tours[k].append(j)
                tour_cost += cost[i][j]
                i = j
                break
        if i == 0:
            break
    tours[k].append(0)
    tour_cost += cost[tours[k][-2]][0]
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_ivestment}")
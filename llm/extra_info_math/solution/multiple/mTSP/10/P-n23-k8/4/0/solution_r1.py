import math
from pulp import *

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

m = 8  # number of robots
n = len(coordinates)  # number of cities including the depot
cities = range(n)

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in cities] for i in cities]

prob = LpProblem("VRP", LpMinimize)
x = LpVariable.dicts("x", (cities, cities, range(m)), 0, 1, LpBinary)
u = LpVariable.dicts("u", (cities), lowBound=0, upBound=n-1, cat=LpContinuous)

# Minimize the total cost
prob += lpSum(x[i][j][k] * cost[i][j] for k in range(m) for i in cities for j in cities if i != j)

# Every city (except depot) visited exactly once
for j in cities:
    if j != 0:
        prob += lpSum(x[i][j][k] for i in cities for k in range(m) if i != j) == 1

# Each robot starts and ends at the depot
for k in range(m):
    prob += lpSum(x[0][j][k] for j in cities if j != 0) == 1
    prob += lpSum(x[i][0][k] for i in cities if i != 0) == 1

# Conservation of flow
for k in range(m):
    for j in cities:
        if j != 0:
            prob += lpSum(x[i][j][k] for i in cities if i != j) == lpSum(x[j][h][k] for h in cities if h != j)

# Subtour elimination
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            for k in range(m):
                prob += u[i] - u[j] + n * x[i][j][k] <= n - 1

prob.solve(PULP_CBC_CMD(msg=False))  # Solve without unnecessary logs from solver

# Extract and display solution
overall_cost = 0
for k in range(m):
    node = 0
    tour = [0]
    tour_cost = 0

    while True:
        found = False
        for j in cities:
            if j != node and x[node][j][k].varValue == 1:
                tour.append(j)
                tour_cost += cost[node][j]
                node = j
                found = True
                break
        if not found:
            break
    if tour[-1] != 0:  # Close the tour if not already closed
        tour.append(0)
        tour_cost += cost[node][0]

    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_cost}")
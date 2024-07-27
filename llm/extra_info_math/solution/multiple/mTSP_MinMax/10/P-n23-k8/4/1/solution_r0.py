import math
from pulp import *

# Defining the coordinate data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}
number_of_robots = 8

# Calculate Euclidean distances between each pair of cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Number of cities including depot
n = len(cities)
m = number_of_robots

# Create the distance matrix
cost = {(i, j): calc_distance(i, j) for i in cities for j in cities if i != j}

# Problem formulation
prob = LpProblem("mTSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)], 0, 1, LpBinary)
u = LpVariable.dicts("u", range(1, n), lowBound=0)

# Objective
prob += lpMax([lpSum([x[i, j, k] * cost[i, j] for i in range(n) for j in range(n) if i != j]) for k in range(m)])

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    prob += lpSum([x[i, j, k] for i in range(n) if i != j for k in range(m)]) == 1

# Each salesman's tour originates and ends at the depot
for k in range(m):
    prob += lpSum([x[0, j, k] for j in range(1, n)]) == 1
    prob += lpSum([x[i, 0, k] for i in range(1, n)]) == 1

# Flow conservation
for k in range(m):
    for j in range(1, n):
        prob += lpSum([x[i, j, k] for i in range(n) if i != j]) == lpSum([x[j, i, k] for i in range(n) if i != j])

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n) * lpSum([x[i, j, k] for k in range(m)]) <= n - 1

# Solve the problem using a suitable solver
prob.solve(PULP_CBC_CMD(msg=False))

# Output results
routes = {k: [0] for k in range(m)}
for k in routes:
    next_city = 0
    while True:
        next_city = next(j for i, j in x if i == next_city and x[i, j, k].varValue == 1)
        if next_city == 0:
            break
        routes[k].append(next_city)

max_cost = 0
for k in range(m):
    route_cost = sum(cost[routes[k][i], routes[k][i + 1]] for i in range(len(routes[k]) - 1))
    routes[k].append(0)  # Complete the tour by adding the return to the depot
    print(f"Robot {k} Tour: {routes[k]}")
    print(f"Robot {k} Total Travel Cost: {route_cost}")
    max_cost = max(max_cost, route_cost)

print(f"Maximum Travel Cost: {max_cost}")
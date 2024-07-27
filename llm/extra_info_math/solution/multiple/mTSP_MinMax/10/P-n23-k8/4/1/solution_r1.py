from math import sqrt
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpInteger

# Constants and city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}
number_of_robots = 8
n = len(cities)

# Problem setup
prob = LpProblem("VRP", LpMinimize)

# Decision Variables
x = LpVariable.dicts('x', [(i, j, k) for i in range(n) for j in range(n) if i != j for k in range(number_of_robots)], cat=LpInteger, lowBound=0, upBound=1)
u = LpVariable.dicts("u", (range(1, n)), lowBound=0, cat='Continuous')

# Helper function to calculate distances
def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
dist = {(i, j): distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Objective
prob += lpSum(x[i, j, k] * dist[i, j] for k in range(number_of_robots) for i in range(n) for j in range(n) if i != j)

# Constraints
for k in range(number_of_robots):
    prob += lpSum(x[0, j, k] for j in range(1, n)) == 1  # Start from depot
    prob += lpSum(x[i, 0, k] for i in range(1, n)) == 1  # Return to depot
    
for j in range(1, n):
    prob += lpSum(x[i, j, k] for i in range(n) if i != j for k in range(number_of_robots)) == 1  # Visit each city exactly once

for k in range(number_of_robots):
    for j in range(1, n):
        prob += lpSum(x[i, j, k] for i in range(n) if i != j) - lpSum(x[j, i, k] for i in range(n) if i != j) == 0

for i in range(1, n):
    for j in range(2, n):
        if i != j:
            for k in range(number_of_robots):
                prob += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solving the problem
prob.solve()

# Output results
max_cost = 0
for k in range(number_of_robots):
    route = []
    for i in range(n):
        for j in range(n):
            if x[i, j, k].varValue == 1:
                route.append(i)
                break
    route.append(0)  # to complete the loop
    route_cost = sum(dist[route[i], route[i+1]] for i in range(len(route)-1))
    print(f"Robot {k} Tour: {route}")
    print(f"Robot {k} Total Travel Cost: {route_cost}")
    if route_cost > max_cost:
        max_cost = route_cost

print(f"Maximum Travel Cost: {max_cost}")
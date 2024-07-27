from pulp import *
import numpy as np

# Define the cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Number of salesmen(robots)
m = 2
# Total number of nodes (cities)
n = len(cities)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(i, j):
    return ((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2) ** 0.5

# Problem formulation
problem = LpProblem("Vehicle_Routing_Problem", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], cat='Binary')
u = LpVariable.dicts("u", [i for i in range(1, n)], lowBound=1, upBound=n-1, cat='Continuous')

# Objective function
problem += lpSum(x[(i, j, k)] * euclidean_distance(i, j) for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    problem += lpSum(x[(i, j, k)] for i in range(n) for k in range(m) if i != j) == 1

# Each salesman leaves each city exactly once and enters each city exactly once
for k in range(m):
    for j in range(1, n):
        problem += lpSum(x[(i, j, k)] for i in range(n) if i != j) - lpSum(x[(j, i, k)] for i in range(n) if i != j) == 0
    # Each salesman should leave the depot exactly once
    problem += lpSum(x[(0, j, k)] for j in range(1, n)) == 1
    problem += lpSum(x[(j, 0, k)] for j in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * lpSum(x[(i, j, k)] for k in range(m)) <= n - 1

# Solve the problem
problem.solve()

# Output tours and total costs
overall_cost = 0
for k in range(m):
    tour = [0]
    while True:
        for j in range(n):
            if x[(tour[-1], j, k)].varValue == 1 and j not in tour:
                tour.append(j)
                break
        if tour[-1] == 0:
            break
    tour_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    overall_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour.preference['Cost']}")

print(f"Overall Total Travel Cost: {overall_cost}")
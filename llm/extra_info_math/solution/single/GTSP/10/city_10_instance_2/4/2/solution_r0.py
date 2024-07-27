import math
from itertools import product
from pulp import *

# City Coordinates
coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# City Groups
city_groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

cities = list(coordinates.keys())
pairs = [(i, j) for i in cities for j in cities if i != j]

# Cost dictionary
costs = {(i, j): euclidean_distance(i, j) for i, j in pairs}

# Model Initialization
model = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", pairs, 0, 1, LpBinary)
u = LpVariable.dicts("u", list(city_groups.keys()), 1, len(city_groups))

# Objective
model += lpSum(costs[i, j] * x[i, j] for i, j in pairs), "Total Travel Cost"

# Constraints
for group_key in city_groups:
    model += lpSum(x[i, j] for i in city_groups[group_key] for j in cities if i != j) == 1
    model += lpSum(x[j, i] for i in city_groups[group_key] for j in cities if i != j) == 1

for i in cities:
    model += lpSum(x[i, j] for j in cities if i != j) - lpSum(x[j, i] for j in cities if i != j) == 0
    
for p, q in product(city_groups.keys(), repeat=2):
    if p != q:
        k = len(city_groups)
        model += u[p] - u[q] + k * lpSum(x[i, j] for i in city_groups[p] for j in city_groups[q]) + (k-2) * lpSum(x[j, i] for i in city_groups[q] for j in city_groups[p]) <= k - 1

# Solve the model
model.solve()

# Extract the solution
tour = []
visited = {0}
current = 0
while True:
    next_city = [j for j in cities if x[current, j].varValue == 1][0]
    tour.append(next_city)
    visited.add(next_city)
    if next_city == 0:
        break
    current = next_city

total_cost = value(model.objective)

# Printing the solution
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
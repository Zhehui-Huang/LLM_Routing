import pulp
import math

# Given city coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Group of cities
city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Distance function between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# PuLP problem setup
problem = pulp.LpProblem("Minimum_Cost", pulp.LpMinimize)

# Variables: x_ij = 1 if path from city i to city j is part of the solution
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective: Minimize total distance
problem += pulp.lpSum(x[(i, j)] * distance(i, j) for i in cities for j in cities if i != j)

# Flow Conservation Constraints
for group in city_groups:
    for i in group:
        problem += pulp.lpSum(x[(j, i)] for j in cities if j != i) - pulp.lpSum(x[(i, j)] for j in cities if j != i) == 0

# Exactly one city from each group must be visited
for group in city_groups:
    problem += pulp.lpSum(x[(0, j)] for j in group) == 1
    problem += pulp.lpSum(x[(j, 0)] for j in group) == 1

# Subtour Elimination Constraints (using Miller-Tucker-Zemlin formulation)
u = pulp.LpVariable.dicts("u", list(cities.keys())[1:], lowBound=1, upBound=len(cities)-1, cat='Continuous')

for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            problem += u[i] - u[j] + (len(cities) - 1) * x[(i, j)] <= len(cities) - 2

# Solve the problem
problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Output the tour and total distance
tour = [0]
current = 0
while len(tour) < 5:
    for j in cities:
        if pulp.value(x[(current, j)]) == 1 and j not in tour:
            tour.append(j)
            current = j
            break
tour.append(0)  # returning to the depot

total_travel_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Print results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
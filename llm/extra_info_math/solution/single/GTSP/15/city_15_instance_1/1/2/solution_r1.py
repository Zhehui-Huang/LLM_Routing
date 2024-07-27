import pulp as pl
import math

# Coordinates of the cities
coordinates = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Grouping of cities
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    c1, c2 = coordinates[city1], coordinates[city2]
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# List of all cities with the depot
cities = sum(groups.values(), [])
cities_with_depot = [0] + cities

# Initialize the problem
prob = pl.LpProblem("Min_Cost_Tour", pl.LpMinimize)

# Variables as x[i, j] for each pair (i, j) where i != j
x = pl.LpVariable.dicts("x", ((i, j) for i in cities_with_depot for j in cities_with_depot if i != j), cat='Binary')

# Objective: Minimize total travel distance
prob += pl.lpSum(x[(i, j)] * distance(i, j) for i in cities_with_depot for j in cities_with_depot if i != j)

# Constraints for connection requirements within and between groups
# Ensure that each group has exactly one exit and one entrance
for group in groups.values():
    prob += pl.lpSum(x[(i, j)] for i in group for j in cities_with_depot if j not in group) == 1  # from
    prob += pl.lpSum(x[(j, i)] for i in group for j in cities_with_depot if j not in group) == 1  # to

# Depot connections
prob += pl.lpSum(x[(0, j)] for j in cities) == 1  # Leaving depot
prob += pl.lpSum(x[(j, 0)] for j in cities) == 1  # Returning to depot

# Flow conservation
for k in cities:
    prob += pl.lpSum(x[(i, k)] for i in cities_with_depot if i != k) == pl.lpSum(x[(k, j)] for j in cities_with_depot if j != k)

# Solve the problem
prob.solve()

# Building the tour based on active x variables
current_city = 0
next_city = None
tour = [current_city]

for _ in range(len(groups) + 1):  # since we need one city from each group plus return
    next_city = next(j for j in cities_with_depot if pl.value(x[(current_city, j)]) == 1)
    tour.append(next_city)
    current_city = next_city

# Compute total travel cost based on the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
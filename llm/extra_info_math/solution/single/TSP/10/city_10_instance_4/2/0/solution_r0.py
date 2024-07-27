import pulp
import math
from itertools import combinations

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# PuLP Model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective
model += pulp.lpSum(x[(i, j)] * distances[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # Leave each city only once
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # Enter each city only once

# Subtour elimination
for s in range(2, n):
    for S in combinations(range(1, n), s):  # Only consider subsets not involving the depot
        model += pulp.lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
model.solve()

# Extract tour
tour = []
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[(i, j)]) == 1:
            tour.append((i, j))

# Format tour correctly starting from depot city 0
def find_next_city(current, tour):
    for i, t in enumerate(tour):
        if t[0] == current:
            return tour.pop(i)

ordered_tour = [0]
next_city = find_next_city(0, tour)
while next_city:
    ordered_tour.append(next_city[1])
    next_city = find_next_city(next_city[1], tour)

ordered_tour.append(0)  # End at the depot

# Calculate total distance
total_cost = sum(distances[ordered_tour[i]][ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))

print("Tour:", ordered_tour)
print("Total travel cost:", total_cost)
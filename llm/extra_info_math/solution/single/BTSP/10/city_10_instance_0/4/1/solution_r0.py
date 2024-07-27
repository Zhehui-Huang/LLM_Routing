import numpy as np
from pulp import LpProblem, LpVariable, lpSum, LpMinimize

# City coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}
n = len(cities)  # Number of cities

# Calculate Euclidean distances between each pair of cities
def distance(p1, p2):
    return np.hypot(p1[0] - p2[0], p1[1] - p2[1])

distances = {(i, j): distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Optimization model
model = LpProblem("Minimize_Max_Distance_between_Cities", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')
dmax = LpVariable("dmax", lowBound=0, cat='Continuous')

# Objective
model += dmax

# Constraints
for i in cities:
    model += lpSum(x[i, j] for j in cities if i != j) == 1  # leave each city once
    model += lpSum(x[j, i] for j in cities if i != j) == 1  # enter each city once

# Max distance constraint
for i in cities:
    for j in cities:
        if i != j:
            model += x[i, j] * distances[i, j] <= dmax

# Subtour elimination constraints
from itertools import combinations
for S in combinations([i for i in cities if i != 0], 2):
    model += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the model
model.solve()

# Output the results
tour = []
for i in cities:
    for j in cities:
        if i != j and x[i, j].varValue > 0.99:
            tour.append((i, j))
            
# Reorder tour starting from the depot 0
ordered_tour = [0]
current_city = 0
for _ in range(len(tour)):
    for i, j in tour:
        if i == current_city:
            ordered_tour.append(j)
            current_city = j
            break

# Calculating total distance and maximum distance between consecutive cities
total_distance = sum(distances[ordered_tour[i], ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))
max_consecutive_distance = max(distances[ordered_tour[i], ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))

print(f"Tour: {ordered_tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")
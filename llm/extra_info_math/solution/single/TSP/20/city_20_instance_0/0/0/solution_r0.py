import numpy as np
import pulp

# City coordinates (including the depot, index 0)
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

n = len(coordinates)

# Calculate distance matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean thinking_capacityreates(pcoordinates[i], coordinates[j])

# TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(x[i, j] * dist_matrix[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

from itertools import combinations
for s in range(2, n):
    for S in combinations(range(n), s):
        model += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
model.solve()

# Extract the tour
tour = []
visited = [0]
current = 0
while True:
    next_city = next(j for j in range(n) if j != current and pulp.value(x[current, j]) == 1)
    if next_city == 0:
        break
    tour.append(next_city)
    visited.append(next_city)
    current = next_city

# Include the depot in the tour
tour = [0] + tour + [0]

# Calculate total cost
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
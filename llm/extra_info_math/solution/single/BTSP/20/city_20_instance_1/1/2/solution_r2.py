import numpy as np
from scipy.spatial.distance import euclidean
from itertools import product
from mip import Model, xsum, minimize, BINARY, OptimizationStatus

# Coordinates for each city, including the depot city at index 0
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23), 
    (78, 76), (68, 45), (50, 28), (69, 9)
]

n = len(cities)  # Total number of cities

# Calculate the Euclidean distance matrix
distances = [[euclidean(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create optimization model
model = Model()

# Decision variables: x[i, j] is 1 if the path goes from city i to city j
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
max_dist = model.add_var()

# Objective: minimize the maximum distance between consecutive cities in the tour
model.objective = minimize(max_dist)

# Constraints
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if j != i) == 1
    model += xsum(x[j][i] for j in range(n) if j != i) == 1

# Max distance constraint: max_dist must be at least as large as every selected distance
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i][j] * distances[i][j] <= max_dist

# Subtour elimination constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += xsum(x[k][l] for k in range(n) for l in range(n)
                     if k != l and (k == i or k == j or l == i or l == j)) <= 3

# Solve the model
status = model.optimize()

if status == OptimizationStatus.OPTIMAL:
    print('Optimal solution found!')

    # Extract the tour
    tour = []
    for i in range(n):
        for j in range(n):
            if x[i][j].x >= 0.99:
                tour.append((i, j))

    # Determine the tour order starting from the depot
    ordered_tour = [0]
    while len(ordered_tour) < n:
        last_city = ordered_tour[-1]
        next_city = next(j for i, j in tour if i == last_city)
        ordered_tour.append(next_city)

    # Calculate tour cost and max distance
    total_cost = sum(distances[ordered_tour[i]][ordered_tour[i+1]] for i in range(n-1))
    max_distance = max(distances[ordered_t ripe places at tour[i]][tour[i+1]] for i in range(n-1))

    # Print results
    ordered_tour.append(0)  # return to the depot
    print("Tour:", ordered_tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("Optimal solution not found. Status code:", status)
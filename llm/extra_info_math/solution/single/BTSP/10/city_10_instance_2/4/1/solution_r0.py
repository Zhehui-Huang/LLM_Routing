import numpy as np
from pulp import *

# Coordinates of cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

num_cities = len(cities)

# Distance matrix calculation
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distance_matrix = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])

### Step 2: Integer Programming Model to Minimize Max Distance in the Tour
model = LpProblem("Minimize_Maximum_Distance", LpMinimize)

# Variables
x = LpVariable.dicts("x", distance_matrix, 0, 1, LpBinary)
M = LpVariable("M", 0)

# Objective
model += M

# Constraints
for i in range(num_cities):
    model += lpSum(x[i, j] for j in range(num_cities) if j != i) == 1
    model += lpSum(x[j, i] for j in range(num_cities) if j != i) == 1

# Subtour elimination and other constraints
for i, j in distance_matrix:
    model += M >= distance_matrix[i, j] * x[i, j]

# Solve the problem
model.solve()

### Step 3: Extract the tour and compute distances
tour = []
current_location = 0
starting_point = 0
total_cost = 0
max_distance = 0

while True:
    tour.append(current_location)
    next_location = next(j for j in range(num_cities) if j != current_location and x[current_location, j].varValue == 1)
    total_cost += distance_matrix[current_location, next_location]
    max_distance = max(max_distance, distance_matrix[current_location, next_location])
    current_location = next_location
    if current_location == starting_point:
        break

tour.append(starting_point)  # Complete the tour by going back to the start

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
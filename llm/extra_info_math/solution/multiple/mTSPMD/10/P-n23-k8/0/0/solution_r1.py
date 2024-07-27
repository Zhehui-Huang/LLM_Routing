import pulp
import numpy as np
from scipy.spatial.distance import cdist

# Data definition
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), 
    (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), 
    (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
num_cities = len(cities_coordinates)
depots = list(range(8))

# Calculate the Euclidean distance matrix
distance_matrix = cdist(cities_coordinates, cities_coordinates)
np.fill_diagonal(distance_matrix, pulp.LpVariable("dummy", lowBound=float('inf')))

# Problem
model = pulp.LpProblem("MDVRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", 
                          ((i, j, k) for k in depots for i in range(num_cities) for j in range(num_cities) if i != j),
                          cat='Binary')

# Objective
model += pulp.lpSum(distance_matrix[i][j] * x[i, j, k] for k in depots for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
for k in depots:
    model += pulp.lpSum(x[k, j, k] for j in range(num_cities) if j != k) == 1 # Depart from depot
    model += pulp.lpSum(x[i, k, k] for i in range(num_cities) if i != k) == 1 # Return to depot

for j in range(num_cities):
    if j not in depots:
        model += pulp.lpSum(x[i, j, k] for k in depots for i in range(num_cities) if i != j) == 1 # Each city visited exactly once

for k in depots:
    for i in range(num_cities):
        if i != k:
            model += pulp.lpSum(x[j, i, k] for j in range(num_cities) if j != i) == \
                     pulp.lpSum(x[i, j, k] for j in range(num_cities) if j != i) # Flow Conservation

# Solve
model.solve()

# Output tour and costs
for k in depots:
    path = [k]
    current = k
    while True:
        next_city = [j for j in range(num_cities) if j != current and pulp.value(x[current, j, k]) == 1]
        if not next_city:
            break
        next_city = next_city[0]
        path.append(next_city)
        current = next_city
        if current == k:
            break

    tour_cost = sum(distance_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
    print(f"Robot {k} Tour: {path}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

overall_cost = sum(distance_matrix[path[i]][path[i+1]] for path in tours for i in range(len(path)-1))
print(f"Overall Total Travel Cost: {overall_cost}")
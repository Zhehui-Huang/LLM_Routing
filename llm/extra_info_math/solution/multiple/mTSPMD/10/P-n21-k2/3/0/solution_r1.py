import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations
import pulp

# Coordinates of cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of cities and depots
num_cities = len(coordinates)
depots = [0, 1]

# Calculate the Euclidean distance matrix
def compute_distance_matrix(coords):
    return distance_matrix(coords, coords)

distance_matrix = compute_distance_readertrix(coordinates)

# Optimization model
model = pulp.LpProblem("Multiple_TSP_VRP", pulp.LpMinimize)

# Variables: x[i, j, k] = 1 if robot k travels from city i to city j
x = pulp.LpVariable.dicts("x", 
                          ((i, j, k) for k in depots for i in range(num_cities) for j in range(num_cities) if i != j),
                          cat='Binary')

# Objective: minimize the total travel cost
model += pulp.lpSum(distance_matrix[i][j] * x[i, j, k] for k in depots for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# Each city must be entered and left only once
for k in depots:
    for j in range(num_cities):
        if j != k:  # Not a depot city
            model += pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j) == pulp.lpSum(x[j, i, k] for i in range(num_cities) if i != j)

# Each robot returns to its depot
for k in depots:
    model += pulp.lpSum(x[k, j, k] for j in range(num_cities) if j != k) == 1
    model += pulp.lpSum(x[j, k, k] for j in range(num_cities) if j != k) == 1

# Subtour elimination
for k in depots:
    u = pulp.LpVariable.dicts(f"u({k})", range(num_cities), lowBound=0, upBound=num_cities-1, cat='Integer')
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j and i != k and j != k:
                model += u[i] - u[j] + (num_cities-1) * x[i, j, k] <= num_cities-2

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Output the results
overall_cost = 0
for k in depots:
    tour = [k]
    current_city = k
    while True:
        next_city = next(j for j in range(num_cities) if pulp.value(x[current_city, j, k]) == 1)
        if next_city == k:
            break
        tour.append(next_city)
        current_city = next_city
    tour.append(k)
    cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    overall_cost += cost
    print(f"Robot starting at depot {k} Tour: {tour}")
    print(f"Robot starting at depot {k} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")
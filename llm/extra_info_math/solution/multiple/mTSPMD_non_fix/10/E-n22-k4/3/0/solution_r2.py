import numpy as np
from math import sqrt
from mip import Model, xsum, minimize, BINARY, INTEGER

# Coordinates of the cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Distance matrix computation
def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

n = len(coordinates)  # Number of cities including depots
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Number of robots and the unique starting depot
n_robots = 4
depot = 0

# Setting up the model
model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
u = [model.add_var(var_type=INTEGER, lb=0) for i in range(n)]

# Objective function
model.objective = minimize(xsum(distances[i][j] * x[i][j] for i in range(n) for j in range(n)))

# Constraints
# Departure and arrival from depot
model += xsum(x[depot][j] for j in range(n) if j != depot) == n_robots
model += xsum(x[j][depot] for j in range(n) if j != depot) == n_robots

# Each city is visited exactly once
for j in range(1, n):
    model += xsum(x[i][j] for i in range(n)) == 1
    model += xsum(x[j][i] for i in range(n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i][j] <= n - 1

# Solve the model
model.optimize()

# Extract tours
tours = {i: [] for i in range(n_robots)}
for i in range(n):
    for j in range(n):
        if x[i][j].x >= 0.99:
            tours[i].append(j)

# Print and evaluate results
total_cost = 0
for i, tour in tours.items():
    if tour:
        tour_cost = sum(distances[tour[k]][tour[k + 1]] for k in range(len(tour) - 1))
        total_cost += tour_cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost}")

print("Overall Total Travel Cost:", total_cost)
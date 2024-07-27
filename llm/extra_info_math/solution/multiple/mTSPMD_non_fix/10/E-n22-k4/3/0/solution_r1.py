import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations
from mip import Model, xsum, minimize, BINARY

# Coordinates of the cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Distance matrix
distances = [[euclidean(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

n = len(coordinates)
n_robots = 4
depots = [0]  # All robots start at depot city 0

# Define the model
model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(n)]

# Objective: Minimize total travel cost
model.objective = minimize(xsum(distances[i][j] * x[i][j] for i in range(n) for j in range(n)))

# Constraints
# Depot constraints
for i in depots:
    model += xsum(x[i][j] for j in range(n) if j != i) == n_robots
    model += xsum(x[j][i] for j in range(n) if j != i) == n_robots

# Each city visited exactly once
for j in range(n):
    if j not in depots:
        model += xsum(x[i][j] for i in range(n)) == 1

for i in range(n):
    if i not in depots:
        model += xsum(x[i][j] for j in range(n)) == 1

# Subtour elimination
for i in range(n):
    for j in range(n):
        if i != j and i not in depots and j not in depots:
            model += u[i] - u[j] + (n + len(depots) - 1) * x[i][j] <= n + len(depots) - 2

# Solve the problem
model.optimize()

# Retrieve results
tours = [[] for _ in range(n_robots)]
for i in range(n):
    for j in range(n):
        if x[i][j].x >= 0.99:
            tours[i].append(j)

# Output the results
robot_tour_costs = []
total_cost = 0
for i, tour in enumerate(tours):
    if tour:
        print(f"Robot {i} Tour:", tour)
        tour_cost = sum(distances[tour[k]][tour[k+1]] for k in range(len(tour)-1))
        robot_tour_costs.append(tour_cost)
        print(f"Robot {i} Total Travel Cost: {tour_cost}")
        total_cost += tour_cost

print("Overall Total Travel Cost:", total_cost)
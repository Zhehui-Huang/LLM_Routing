import cvxpy as cp
import numpy as np
import math

# Define the coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Define the demands of each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_cities = len(coordinates)
num_robots = 8
vehicle_capacity = 35

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

cost_matrix = np.array([
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
])

# CVXPY model setup
x = cp.Variable((num_robots, num_cities, num_cities), boolean=True)

# Objective function: minimize the total travel cost
objective = cp.Minimize(cp.sum(cp.multiply(cost_matrix, cp.sum(x, axis=0))))

# Constraints
constraints = []

# Each city is visited exactly once
for j in range(1, num_cities):
    constraints.append(cp.sum(x[:, j, :]) == 1)

# Each robot departs and arrives at the depot
for r in range(num_robots):
    constraints.append(cp.sum(x[r, 0, :]) == 1)
    constraints.append(cp.sum(x[r, :, 0]) == 1)

# Flow conservation constraints
for r in range(num_robots):
    for j in range(1, num_cities):
        constraints.append(cp.sum(x[r, j, :]) == cp.sum(x[r, :, j]))

# Capacity constraints
for r in range(num_robots):
    constraints.append(cp.sum(cp.multiply(demands, cp.sum(x[r, :, :], axis=0))) <= vehicle_capacity)

# Solve the problem
problem = cp.Problem(objective, constraints)
problem.solve(solver=cp.GLPK_MI)

# Solution extraction and formatting
# Here you would extract the solution from `x.value` and decode it into routes, calculate total costs